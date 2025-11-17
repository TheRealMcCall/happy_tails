from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Category, Product, Variant, Stock, Wishlist


class ProductModelTests(TestCase):
    """Tests for the Product model."""

    def setUp(self):
        self.category = Category.objects.create(
            name="Dog Toys",
            slug="dog-toys",
            description="dog toys category"
        )
        self.product = Product.objects.create(
            category=self.category,

            name="Rope Toy",
            description="Strong rope toy",
            slug="rope-toy",
            # image is optional (null=True, blank=True)
            # is_available has a default of True
        )

    def test_product_str_returns_name(self):
        """__str__ on Product should return the product name."""
        self.assertEqual(str(self.product), "Rope Toy")

    def test_get_absolute_url_uses_slug(self):
        """
        get_absolute_url should return the product_detail URL
        using the products slug
        """
        url = self.product.get_absolute_url()
        expected_url = reverse(
            "store:product_detail",
            args=[self.product.slug]
            )
        self.assertEqual(url, expected_url)


class VariantAndStockModelTests(TestCase):
    """Tests for Variant and Stock models."""

    def setUp(self):
        category = Category.objects.create(
            name="Cat Food",
            slug="cat-food",
        )
        self.product = Product.objects.create(
            category=category,
            name="Salmon Kibble",
            description="Tasty kibble for cats.",
            slug="salmon-kibble",
        )
        self.variant = Variant.objects.create(
            product=self.product,
            price="9.99",
            sku="HT-CAT-001",
            # size/colour are optional (blank=True)
        )
        self.stock = Stock.objects.create(
            variant=self.variant,
            quantity=5,
            low_stock_threshold=2,
        )

    def test_variant_str_includes_product_and_sku(self):
        """__str__ on Variant should show product name and SKU."""
        self.assertEqual(str(self.variant), "Salmon Kibble [HT-CAT-001]")

    def test_stock_str_shows_sku_and_quantity(self):
        """__str__ on Stock should show the SKU and quantity."""
        self.assertEqual(str(self.stock), "HT-CAT-001 → 5")


class WishlistModelTests(TestCase):
    """Tests for the Wishlist model."""

    def test_wishlist_str_uses_username(self):
        """
        __str__ on Wishlist should be in the format:
        "<username>'s Wishlist"
        """
        User = get_user_model()
        user = User.objects.create_user(
            username="wishlist_user",
            email="wishlist@example.com",
            password="testpass123",
        )
        wishlist, _ = Wishlist.objects.get_or_create(user=user)
        self.assertEqual(str(wishlist), "wishlist_user's Wishlist")


class StoreViewTests(TestCase):
    """Tests for public store views."""

    def setUp(self):
        self.category = Category.objects.create(
            name="Small Pets",
            slug="small-pets",
        )
        self.product = Product.objects.create(
            category=self.category,
            name="Hamster Wheel",
            description="Quiet running wheel.",
            slug="hamster-wheel",
        )

    def test_home_page_renders(self):
        """Home page should return HTTP 200 and use the correct template."""
        url = reverse("store:home")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "store/home.html")

    def test_product_list_shows_product(self):
        """
        Product list view should return HTTP 200 and include
        the product name in the response.
        """
        url = reverse("store:product_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)
