from django.test import TestCase
from django.urls import reverse

from store.models import Category, Product, Variant, Stock


class BasketTests(TestCase):
    """Tests for basket add/update behaviour."""

    def setUp(self):
        # Create a simple product + variant + stock
        # so we can add it to a basket
        category = Category.objects.create(
            name="Dog Treats",
            slug="dog-treats",
        )
        self.product = Product.objects.create(
            category=category,
            name="Chewy Bones",
            description="Tasty bones for dogs.",
            slug="chewy-bones",
        )
        self.variant = Variant.objects.create(
            product=self.product,
            price="4.50",
            sku="HT-DOG-001",
        )
        # Stock must exist
        # otherwise add_to_basket will think it's out of stock
        Stock.objects.create(
            variant=self.variant,
            quantity=10,
            low_stock_threshold=3,
        )

    def test_add_to_basket_stores_quantity_in_session(self):
        """
        Posting to basket:add_to_basket should create a 'basket'
        in the session and store the requested quantity.
        """
        url = reverse("basket:add_to_basket")
        response = self.client.post(
            url,
            {"variant": self.variant.id, "qty": 2},
            follow=False,
        )

        # The view should redirect back to the product list
        self.assertRedirects(response, reverse("store:product_list"))

        # The session should now contain a "basket" key
        session = self.client.session
        basket = session.get("basket")
        self.assertIsNotNone(basket)

        # Basket keys are stored as strings of the variant ID
        self.assertIn(str(self.variant.id), basket)
        self.assertEqual(basket[str(self.variant.id)], 2)
