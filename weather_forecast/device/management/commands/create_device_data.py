import random
from datetime import timedelta

from django.core.management import BaseCommand, CommandError
from django.utils import timezone

from device.models import Device, Data
from user.models import Profile


class Command(BaseCommand):
    help = 'Creates fake data for testing'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        devices_count = options['count']
        if devices_count < 0:
            raise CommandError('Devices count must be bigger than one')
        if not Profile.objects.count():
            raise CommandError('You need to create at least one user')

        last_device_id = 0
        last_device = Device.objects.all().order_by('-id').first()
        if last_device:
            last_device_id = last_device.id

        for i in range(devices_count):
            random_user = Profile.objects.all().order_by('?').first()
            device = Device.objects.create(
                user=random_user,
                name=f'Device no. {last_device_id+i}',
                localization=f'Localization #{last_device_id+i}',
                device=random.choice(Device.DEVICE_CHOICES)[0]
            )

            now = timezone.now()

            Data.objects.bulk_create([
                Data(
                    device=device,
                    datetime=now - timedelta(minutes=i),
                    precipitation = random.randint(0, 100),
                    humidity = random.randint(0, 100),
                    temperature = random.randint(0, 100),
                    pressure = random.randint(0, 100),
                    exposition = random.randint(0, 100),
                    wind_speed = random.randint(0, 100),
                )
                for i in range(100)
            ])
        self.stdout.write(self.style.SUCCESS(f'Successfully created {devices_count} devices'))
