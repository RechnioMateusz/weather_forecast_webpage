"""File determining this directory as user application."""

from django.apps import AppConfig


class UserConfig(AppConfig):
    """Configuration for user application.

    **Attributes**
        :name: Name of application. [str]
    """

    name = "user"
