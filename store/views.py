from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from django.db.models import Q
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import ProductForm


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


def superuser_required(view_func):
    return login_required(
        user_passes_test(lambda u: u.is_superuser)(view_func)
    )


@superuser_required
def manage_dashboard(request):
    """Render the superuser dashboard for managing products."""

    products = (
        Product.objects
        .select_related("category")
        .order_by("name")
    )

    context = {"products": products}
    return render(request, "store/manage/dashboard.html", context)


@superuser_required
def product_create(request):
    """Create a product."""
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, f'Created “{product.name}”.')
            return redirect("store:manage_dashboard")
    else:
        form = ProductForm()
    return render(
        request,
        "store/product_form.html",
        {"form": form, "is_create": True},
    )


@superuser_required
def product_edit(request, pk):
    """Edit an existing product."""
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Updated “{product.name}”.')
            return redirect("store:manage_dashboard")
    else:
        form = ProductForm(instance=product)
    return render(
        request,
        "store/product_form.html",
        {"form": form, "product": product, "is_create": False},
    )


@superuser_required
def product_delete(request, pk):
    """Delete a product after confirmation."""
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        name = product.name
        product.delete()
        messages.success(request, f'Deleted “{name}”.')
        return redirect("store:manage_dashboard")
    return render(
        request,
        "store/manage/product_delete.html",
        {"product": product},
    )
