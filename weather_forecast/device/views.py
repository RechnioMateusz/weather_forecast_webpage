"""Views for device application."""

from django.shortcuts import render
from rest_framework import viewsets

from .models import Device, Data
from .serializers import DeviceSerializer, DataSerializer


def main_view(request):
    """Main view for device application. Displays info about devices.

    ===========================================================================
    |                      ONLY FOR DEBBUGING PURPOSES                        |
    ===========================================================================
    """

    return render(
        request=request,
        template_name="user/main.html",
        context={
            "profiles": Device.objects.all()
        }
    )

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DataViewSet(viewsets.ModelViewSet):
    serializer_class = DataSerializer

    def get_queryset(self):
        return Data.objects.filter(device=self.kwargs['device_pk'])
