from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    """Inline for displaying order items on the order admin page."""
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Admin configuration for orders with inline order items."""
    list_display = ("order_number",
                    "user",
                    "total",
                    "created_at"
                    )
    inlines = [OrderItemInline]
