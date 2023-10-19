from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Model


# Create your models here.

class Thing(AbstractUser):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=40)
    quantity = models.IntegerField()
