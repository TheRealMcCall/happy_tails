from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(
        max_length=120,
        unique=True
    )
    slug = models.SlugField(
        max_length=120,
        unique=True
    )
    description = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT,
        related_name="products"
        )
    image = models.ForeignKey(
        "ProductImage", on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="product_image"
        )
    name = models.CharField(
        max_length=160
        )
    slug = models.SlugField(
        max_length=180,
        unique=True
        )
    is_available = models.BooleanField(
        default=True
        )
    created_on = models.DateTimeField(
        auto_now_add=True
        )

    def __str__(self):
        return self.name


class Variant(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="variants"
        )
    image = CloudinaryField(
        "image",
        blank=True,
        null=True
        )
    size = models.CharField(
        max_length=60,
        blank=True
        )
    colour = models.CharField(
        max_length=60,
        blank=True
        )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
        )
    sku = models.CharField(
        max_length=64,
        unique=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.product.name} [{self.sku}]"


class Stock(models.Model):
    variant = models.OneToOneField(
        Variant, on_delete=models.CASCADE,
        related_name="stock"
        )
    quantity = models.PositiveIntegerField(
        default=0
        )
    low_stock_threshold = models.PositiveIntegerField(
        default=0
        )

    def __str__(self):
        return f"{self.variant.sku} → {self.quantity}"


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name="images",
        null=True,
        blank=True)
    variant = models.ForeignKey(
        Variant, on_delete=models.CASCADE,
        related_name="images",
        null=True,
        blank=True
        )
    image = CloudinaryField(
        "image",
        blank=True,
        null=True)
    alt_text = models.CharField(
        max_length=160,
        blank=True)
    caption = models.CharField(
        max_length=255,
        blank=True)
    created_on = models.DateTimeField(
        auto_now_add=True
        )
    is_thumbnail = models.BooleanField(
        default=False
        )

    def __str__(self):
        return self.alt_text or f"Image #{self.pk}"
