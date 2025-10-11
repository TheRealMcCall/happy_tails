from django.conf import settings
from django.db import models
from cloudinary.models import CloudinaryField
from django.urls import reverse


class Category(models.Model):
    """Model for product categories"""
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
        """Returns category name in admin"""
        return self.name


class Product(models.Model):
    """Model for products within a category"""
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
    description = models.TextField(
        blank=True
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
        """Return the product name."""
        return self.name

    def get_absolute_url(self):
        """Return the URL for the product detail view."""
        return reverse("store:product_detail", args=[self.slug])

    def get_product_image(self):
        """ Return the image for the product. """
        return self.image or self.images.first()


class Variant(models.Model):
    """Model representing a product variantion such as size or colour."""
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
        """Return formatted product name and SKU"""
        return f"{self.product.name} [{self.sku}]"


class Stock(models.Model):
    """Model for tracking stock levels for each variant."""
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
        """Returns variant SKU and current stock quantity"""
        return f"{self.variant.sku} → {self.quantity}"


class ProductImage(models.Model):
    """Model for storing images linked to products or variants"""
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
        """Return alt text or image ID."""
        return self.alt_text or f"Image #{self.pk}"


class ProductReview(models.Model):
    """Model for customer ratings for products."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
        )
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='reviews'
        )
    rating = models.PositiveSmallIntegerField(
        choices=[(i, i) for i in range(1, 6)]
        )
    comment = models.TextField(
        blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True)

    def __str__(self):
        """Return formatted review summary."""
        return f"{self.product.name} - {self.rating}★ by {self.user.username}"


class Wishlist(models.Model):
    """Model for a user to store a wishlist of products."""
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='wishlist')
    products = models.ManyToManyField(
        'Product',
        blank=True,
        related_name='wishlisted_by')

    def __str__(self):
        """Return easy to read wishlist label"""
        return f"{self.user.username}'s Wishlist"
