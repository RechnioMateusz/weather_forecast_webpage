"""File determining this directory as forecast application."""

from django.apps import AppConfig


class ForecastConfig(AppConfig):
    """Configuration for forecast application.

    **Attributes**
        :name: Name of application. [str]
    """

    name = 'forecast'
