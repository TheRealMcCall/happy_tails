from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Profile, Address


class ProfileModelTests(TestCase):
    """Tests for the Profile model."""

    def test_profile_str_uses_username(self):
        """__str__ on Profile should return 'Profile for <username>'"""

        User = get_user_model()
        user = User.objects.create_user(
            username="luke_tester",
            email="luke@example.com",
            password="testpass123",
        )
        profile = Profile.objects.get(user=user)

        self.assertEqual(str(profile), "Profile for luke_tester")


class AddressModelTests(TestCase):
    """Tests for the Address model."""

    def test_address_str_joins_label_and_parts(self):
        """
        __str__ on Address should join label, first_line, city, postcode
        with commas, skipping any empty parts.
        """
        User = get_user_model()
        user = User.objects.create_user(
            username="address_user",
            email="address@example.com",
            password="testpass123",
        )

        address = Address.objects.create(
            user=user,
            label="Home",
            first_line="1 Test Street",
            city="Bangor",
            postcode="BT20 0AA",
            # second_line is optional (blank=True)
            # country has a default of "United Kingdom"
        )

        self.assertEqual(str(address), "Home, 1 Test Street, Bangor, BT20 0AA")
