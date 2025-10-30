from django import forms
from .models import Product, Variant, Stock


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


class VariantForm(forms.ModelForm):
    class Meta:
        model = Variant
        fields = [
            "size",
            "colour",
            "price",
            "sku",
            "is_available"]


class ProductPickForm(forms.Form):
    product = forms.ModelChoiceField(
        queryset=Product.objects.order_by("name"),
        label="Product",
        empty_label="Select a product",
    )


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["quantity", "low_stock_threshold"]
