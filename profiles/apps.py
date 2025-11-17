from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """Application configuration for the profiles app."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'

    def ready(self):
        from . import signals
