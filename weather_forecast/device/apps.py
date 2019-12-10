"""File determining this directory as device application."""

from django.apps import AppConfig


class DeviceConfig(AppConfig):
    """Configuration for device application.

    **Attributes**
        :name: Name of application. [str]
    """

    name = 'device'
