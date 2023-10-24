from django.db import models
from django.db.models import Model


# Create your models here.

class Thing(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=40)
    quantity = models.IntegerField()
