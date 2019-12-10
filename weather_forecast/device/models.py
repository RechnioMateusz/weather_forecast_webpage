"""Models for device applications."""

from django.db import models


class Device(models.Model):
    """Weather forecast device model. Stores data about device name,
    localization and type.

    **Attributes**
        :user: Foreign key to user profile. [django.db.models.ForeignKey]
        :name: Device name. [django.db.models.CharField]
        :localization: Device localization. [django.db.models.CharField]
        :device: Device type. [django.db.models.CharField]
    """

    user = models.ForeignKey(to="user.Profile", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    localization = models.CharField(max_length=100)
    device = models.CharField(
        max_length=10,
        choices=[
            ("RPi 4B", "Raspberry Pi 4 model B"),
            ("RPi 3A+", "Raspberry Pi 3 model A+"),
            ("RPi 3B+", "Raspberry Pi 3 model B+"),
            ("RPi 3B", "Raspberry Pi 3 model B"),
            ("RPi 2B", "Raspberry Pi 2 model B"),
            ("RPi 1B+", "Raspberry Pi 1 model B+"),
            ("RPi 1A+", "Raspberry Pi 1 model A+"),
            ("RPi 0W", "Raspberry Pi Zero W"),
            ("RPi 0", "Raspberry Pi Zero"),
        ]
    )

    def __str__(self):
        return f"{self.name} {self.device}"


class Data(models.Model):
    """Single data measurement model. Stores data about weather conditions.

    **Attributes**
        :device: Foreign key to device. [django.db.models.ForeignKey]
        :datetime: Datetime of measurement. [django.db.models.DateTimeField]
        :precipitation: Measured precipitation. [django.db.models.FloatField]
        :humidity: Measured humidity. [django.db.models.FloatField]
        :temperature: Measured temperature. [django.db.models.FloatField]
        :pressure: Measured pressure. [django.db.models.FloatField]
        :exposition: Measured exposition. [django.db.models.FloatField]
        :wind_speed: Measured wind speed. [django.db.models.FloatField]
    """

    device = models.ForeignKey(to=Device, on_delete=models.SET_NULL, null=True)
    datetime = models.DateTimeField()
    precipitation = models.FloatField()
    humidity = models.FloatField()
    temperature = models.FloatField()
    pressure = models.FloatField()
    exposition = models.FloatField()
    wind_speed = models.FloatField(default=0)

    def __str__(self):
        return f"{self.device.name} {self.date}"
