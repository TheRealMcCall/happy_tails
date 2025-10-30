from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, ProductImage
from django.db.models import Q
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import ProductForm, VariantForm, ProductPickForm
from django.urls import reverse


def home(request):
    """Render the store home page."""
    return render(request, "store/home.html")


def product_list(request, category_slug=None):
    """List available products with category and search filters."""
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
    """Display a single product detail page."""
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
            image_upload = form.cleaned_data.get("upload")
            if image_upload:
                image = ProductImage(product=product, image=image_upload)
                image.save()
                if not product.image:
                    product.image = image
                    product.save(update_fields=["image"])
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
            product = form.save()
            image_upload = form.cleaned_data.get("upload")
            if image_upload:
                image = ProductImage(product=product, image=image_upload)
                image.save()
                product.image = image
                product.save(update_fields=["image"])
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


@superuser_required
def variant_choose_product(request):
    """Choose product to adjust variant"""
    if request.method == "POST":
        form = ProductPickForm(request.POST)
        if form.is_valid():
            product = form.cleaned_data["product"]
            return redirect(
                reverse("store:variant_create", args=[product.pk]))
    else:
        form = ProductPickForm()
    return render(request, "store/manage/variant_picker.html", {"form": form})


@superuser_required
def variant_create(request, pk):
    """Create a variant for a product"""
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = VariantForm(request.POST)
        if form.is_valid():
            variant = form.save(commit=False)
            variant.product = product
            variant.save()
            messages.success(request, "Variant added.")
            return redirect(
                reverse("store:manage_dashboard")
                )
    else:
        form = VariantForm()

    return render(
        request,
        "store/manage/variant_form.html",
        {"product": product, "form": form},
    )
