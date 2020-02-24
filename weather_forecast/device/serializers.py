from rest_framework import serializers

from .models import Device, Data


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['user', 'name', 'localization', 'device']


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'