from django.apps import AppConfig


class BasketConfig(AppConfig):
    """Application configuration for the basket app."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'basket'
