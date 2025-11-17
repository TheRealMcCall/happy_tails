from django.contrib import admin
from .models import Profile, Address


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Admin configuration for user profiles and saved addresses."""
    list_display = (
        "user",
        "first_name",
        "last_name",
        "phone_number",
        "default_delivery_address",
        "default_billing_address"
        )
    search_fields = (
        "user__username",
        "user__email",
        "first_name",
        "last_name",
        "phone_number"
        )
    autocomplete_fields = (
        "default_delivery_address",
        "default_billing_address")


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    """Admin configuration for customer addresses."""
    list_display = (
        "user",
        "label",
        "first_line",
        "city",
        "postcode",
        "country",
        "phone_number"
        )
    search_fields = (
        "user__username",
        "user__email",
        "label",
        "first_line",
        "city",
        "postcode"
        )
    list_filter = (
        "country",
        )
    autocomplete_fields = (
        "user",
        )
