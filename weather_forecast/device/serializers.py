from datetime import datetime

from rest_framework import serializers
from .models import Device, Data

class UnixTimestampField(serializers.Field):
    def to_representation(self, value):
        epoch = datetime(1970, 1, 1)
        return (value - epoch).total_seconds()

    def to_internal_value(self, data):
        return datetime.utcfromtimestamp(data)

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class DataSerializer(serializers.ModelSerializer):
    datetime = UnixTimestampField()

    class Meta:
        model = Data
        fields = '__all__'
