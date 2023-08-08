from django.db import models

from django.conf import settings
from django.contrib.auth import get_user_model


class Book(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)