from django.shortcuts import render, get_object_or_404
from .models import Product


def home(request):
    return render(request, "store/home.html")


def product_list(request):
    products = Product.objects.all().select_related("category")
    return render(request, "store/product_list.html", {"products": products})


def product_detail(request, slug):
    product = get_object_or_404(
        Product.objects.select_related('category').prefetch_related('variants__stock'),
        slug=slug,
    )

    return render(request, 'store/product_details.html', {'product': product})
