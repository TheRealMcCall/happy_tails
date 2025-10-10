from django.conf import settings
from django.db import models

# Create your models here.


class Profile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )

    first_name = models.CharField(
        max_length=30,
        blank=True)
    last_name = models.CharField(
        max_length=30,
        blank=True)
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text="Contact Number (Optional)",
    )

    default_delivery_address = models.ForeignKey(
        "profiles.Address",
        on_delete=models.SET_NULL,
        related_name="profile_delivery_address",
        blank=True,
        null=True,
        help_text="User’s preferred delivery address.",
    )

    default_billing_address = models.ForeignKey(
        "profiles.Address",
        on_delete=models.SET_NULL,
        related_name="profile_billing_address",
        blank=True,
        null=True,
        help_text="User’s preferred billing address.",
    )

    created_at = models.DateTimeField(
        auto_now_add=True
        )
    updated_at = models.DateTimeField(
        auto_now=True
        )

    class Meta:
        ordering = ["user__username"]

    def __str__(self):
        username = getattr(self.user, "username", None) or getattr(self.user, "email", "")
        return f"Profile for {username}"


class Address(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="addresses"
        )
    label = models.CharField(
        max_length=30,
        blank=True,
        help_text="Optional name, e.g. Home or Work Address"
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

    def __str__(self):
        parts = [self.label, self.first_line, self.city, self.postcode]
        return ", ".join([p for p in parts if p])
