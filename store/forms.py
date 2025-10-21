from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "category",
            "image",
            "name",
            "description",
            "slug",
            "is_available",
            ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
        }
