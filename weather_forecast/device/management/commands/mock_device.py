import time
import random

import requests
from django.core.management import BaseCommand, CommandError

from device.models import Device


class Sensor:
    SENSOR_UNITS = {
        "precipitation": "%",
        "humidity": "%",
        "temperature": "C",
        "pressure": "hPa",
        "exposition": "lm",
        "wind_speed": "m/s",
    }

    def __init__(self, name):
        if name in Sensor.SENSOR_UNITS:
            self._name = name
            self._unit = Sensor.SENSOR_UNITS.get(name)
        else:
            raise CommandError(f"{name} is invalid sensor")

    @property
    def name(self):
        return self._name

    @property
    def unit(self):
        return self._unit


class Command(BaseCommand):
    help = "Starts mocking specified device. If You need some endpoint to test mocking use https://beeceptor.com/"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.device_id = None
        self.endpoint = None

        self.sensors = [
            Sensor(name="precipitation"),
            Sensor(name="humidity"),
            Sensor(name="temperature"),
            Sensor(name="pressure"),
            Sensor(name="exposition"),
            Sensor(name="wind_speed"),
        ]

    def add_arguments(self, parser):
        parser.add_argument(
            "device_id", type=int,
            help="Mocked device ID\n\tFirstly add it to database"
        )
        parser.add_argument(
            "endpoint", type=str,
            help="Endpoint address to send data to"
        )

    def get_random_data(self):
        sensor = random.choice(self.sensors)

        return {
            "device_id": self.device_id,
            "timestamp": time.time(),
            "source": sensor.name,
            "value": random.random() * 100,
            "unit": sensor.unit,
        }

    def check_options(self, options):
        self.device_id = options.pop("device_id")
        self.endpoint = options.pop("endpoint")

        if not Device.objects.filter(id=self.device_id).first():
            raise CommandError(
                f"Invalid device ID. Possible devices: {Device.objects.all()}"
            )

    def handle(self, *args, **options):
        self.check_options(options=options)

        self.stdout.write(
            self.style.SUCCESS(f"Starting device {self.device_id} mock")
        )

        while True:
            try:
                time.sleep(1)
                requests.post(url=self.endpoint, data=self.get_random_data())
            except KeyboardInterrupt:
                self.stdout.write(
                    self.style.SUCCESS(f"Stoping device {self.device_id} mock")
                )
                break
