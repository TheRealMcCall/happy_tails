from django.apps import AppConfig


class StoreConfig(AppConfig):
    """Configuration for the store application."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store'

    def ready(self):
        """Import signal handlers when the app is ready."""
        from . import signals
