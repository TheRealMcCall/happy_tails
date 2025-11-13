from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class CheckoutViewTests(TestCase):
    """Tests for the checkout view behaviour."""

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username="checkout_user",
            email="checkout@example.com",
            password="testpass123",
        )

    def test_checkout_redirects_when_basket_empty(self):
        """
        If the basket is empty, checkout_view should redirect to
        the basket:view_basket page.
        """
        # login_required decorator means we must be logged in first
        self.client.force_login(self.user)

        url = reverse("checkout:start")
        response = self.client.get(url)

        self.assertRedirects(response, reverse("basket:view_basket"))
