"""Models for user application."""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """User profile model. In future it will propably also store localization
    data.

    **Attributes**
        :user: One to one field with user model.
               [django.db.models.OneToOneField]
    """

    user = models.OneToOneField(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username)
