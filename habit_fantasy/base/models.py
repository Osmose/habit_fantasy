from enum import Enum

from django.contrib.auth.models import User
from django.db import models


class Difficulty(Enum):
    trivial = 0
    easy = 5
    medium = 10
    difficult = 15


class Habit(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=255)
    difficulty = models.IntegerField(choices=[(d.value, d.name) for d in Difficulty])
