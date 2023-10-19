from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Model


# Create your models here.

class User(AbstractUser):
    name = models.TextField()
    description = models.CharField(max_length=20)
    quantity = models.IntegerField()
