from django.contrib import admin
from .models import Category, Product, Variant, Stock, ProductImage

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Variant)
admin.site.register(Stock)
admin.site.register(ProductImage)
