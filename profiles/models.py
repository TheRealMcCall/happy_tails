from django.conf import settings
from django.db import models

# Create your models here.


class Address(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="addresses"
        )
    first_name = models.CharField(
        max_length=30
        )
    last_name = models.CharField(
        max_length=30
        )
    email = models.EmailField(
        blank=True
        )
    first_line = models.CharField(
        max_length=80
        )
    second_line = models.CharField(
        max_length=80,
        blank=True
        )
    city = models.CharField(
        max_length=30
        )
    postcode = models.CharField(
        max_length=20
        )
    country = models.CharField(
        max_length=25,
        default="United Kingdom"
        )
    phone_number = models.CharField(
        max_length=30,
        blank=True
        )
    default_address = models.BooleanField(
        default=False
        )
    billing_address = models.BooleanField(
        default=False
        )
    delivery_address = models.BooleanField(
        default=False
        )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
