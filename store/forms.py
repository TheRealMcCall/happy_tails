from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    upload = forms.ImageField(required=False, label="Upload new image")

    class Meta:
        model = Product
        fields = [
            "category",
            "name",
            "description",
            "slug",
            "is_available",
            "upload",
            ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
        }
