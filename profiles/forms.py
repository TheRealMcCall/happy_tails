from django import forms
from .models import Profile, Address


class ProfileForm(forms.ModelForm):
    """Form for user profile details"""
    class Meta:
        model = Profile
        fields = ["first_name", "last_name",]


class AddressForm(forms.ModelForm):
    """Form for Creating an Address for the user"""
    class Meta:
        model = Address
        fields = [
            "label",
            "first_line",
            "second_line",
            "city",
            "postcode",
            "country",
            "phone_number",
        ]
