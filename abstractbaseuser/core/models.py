from django.db import models
from users.models import CustomUser
from django.conf import settings


"""
class Course(models.Model):
    slug = models.SlugField(max_length=100)
    name = models.CharField(max_length=100)
    tutor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
"""


class Course(models.Model):
    slug = models.SlugField(max_length=100)
    name = models.CharField(max_length=100)
    tutor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Book(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)