from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db.models import Q


def home(request):
    return render(request, "store/home.html")


def product_list(request, category_slug=None):
    products = (
        Product.objects.filter(is_available=True)
        .select_related("category")
        .prefetch_related("images")
    )

    active_category = None
    if category_slug:
        active_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=active_category)

    q = request.GET.get("q", "").strip()
    if q:
        products = (
            products.filter(
                Q(name__icontains=q)
                | Q(description__icontains=q)
                | Q(variants__sku__icontains=q)
            )
            .distinct()
        )

    categories = Category.objects.all().order_by("name")

    return render(
        request,
        "store/product_list.html",
        {
            "products": products,
            "categories": categories,
            "active_category": active_category,
            "q": q,
        },
    )


def product_detail(request, slug):
    product = get_object_or_404(
        Product.objects
        .select_related('category')
        .prefetch_related('variants__stock'),
        slug=slug,
    )

    return render(request, 'store/product_details.html', {'product': product})
