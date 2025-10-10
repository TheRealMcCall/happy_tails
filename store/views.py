from django.shortcuts import render
from .models import Product
# Create your views here.


def home(request):
    return render(request, "store/home.html")


def product_list(request):
    products = Product.objects.all().select_related("category")
    return render(request, "store/product_list.html", {"products": products})
