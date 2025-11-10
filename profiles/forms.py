from django import forms
from .models import Profile, Address
from localflavor.gb.forms import GBPostcodeField
from phonenumber_field.formfields import PhoneNumberField


class ProfileForm(forms.ModelForm):
    """Form for user profile details"""
    class Meta:
        model = Profile
        fields = ["first_name", "last_name",]


class AddressForm(forms.ModelForm):
    """Form for Creating an Address for the user"""
    phone_number = PhoneNumberField(region="GB", required=True,
                                    widget=forms.TextInput(attrs={
                                        "inputmode": "tel",
                                        "autocomplete": "tel",
                                        "placeholder": "Enter phone number",
                                    }))
    postcode = GBPostcodeField(widget=forms.TextInput(attrs={
        "placeholder": "Enter post code",
        "autocomplete": "postal-code",
    }))

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

    def clean_phone_number(self):
        n = self.cleaned_data.get("phone_number")
        return n.as_e164 if n else n
