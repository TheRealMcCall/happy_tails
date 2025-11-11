from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Wishlist


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_wishlist_for_user(sender, instance, created, **kwargs):
    if created:
        Wishlist.objects.get_or_create(user=instance)
