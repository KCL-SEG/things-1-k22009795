from django.db import models
from django.db.models import Model



# Create your models here.

from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator

class Thing(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        blank=False,
        validators=[RegexValidator(
            regex=r'^\w{1,30}$',
            message='Username must be unique, not blank, and have no more than 30 characters'
        )]
    )
    description = models.CharField(
        max_length=120,
        unique=False,
        blank=True,
        validators=[RegexValidator(
            regex=r'^.{0,120}$',
            message='Description can have up to 120 characters'
        )]
    )
    quantity = models.IntegerField(
        unique=False,
        validators=[
            MaxValueValidator(100, message='Quantity cannot be more than 100'),
            MinValueValidator(0, message='Quantity cannot be less than 0')
        ]
    )