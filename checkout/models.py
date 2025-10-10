from django.conf import settings
from django.db import models
from profiles.models import Address
from store.models import Variant


class Order(models.Model):
    """Order Model"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="orders"
    )
    billing_address = models.ForeignKey(
        Address,
        on_delete=models.PROTECT,
        related_name="order_billing_address"
    )
    delivery_address = models.ForeignKey(
        Address,
        on_delete=models.PROTECT,
        related_name="order_delivery_address"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
        )
    stripe_session_id = models.CharField(
        max_length=255, blank=True
        )
    sub_total = models.DecimalField(
        max_digits=10,
        decimal_places=2
        )
    total = models.DecimalField(
        max_digits=10, decimal_places=2
        )
    order_number = models.CharField(
        max_length=20, unique=True
        )
    email = models.EmailField()

    def __str__(self):
        return f"Order {self.order_number} - {self.user.username}"


class OrderItem(models.Model):
    """Order Item Model"""
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )
    variant = models.ForeignKey(
        Variant,
        on_delete=models.PROTECT
    )
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
        )

    def __str__(self):
        return f"{self.variant} x {self.quantity}"
