from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from store.models import Variant
from django.contrib import messages
from django.views.decorators.http import require_POST


def _basket(request):
    """Return the session basket, creating it if missing."""
    return request.session.setdefault("basket", {})


def add_to_basket(request):
    """Add a variant to the session basket and redirect to the basket view."""
    variant_id = request.POST.get("variant_id")
    if not variant_id:
        return redirect("store:product_list")

    try:
        requested_quantity = max(1, int(request.POST.get("qty", "1")))
    except ValueError:
        requested_quantity = 1

    variant = get_object_or_404(
        Variant.objects.select_related("stock"),
        pk=variant_id,
    )

    available_quantity = (
        getattr(getattr(variant, "stock", None), "quantity", 0) or 0
    )

    if available_quantity <= 0 or requested_quantity > available_quantity:
        messages.error(request, "Sorry, not enough stock.")
        return redirect("store:product_detail", slug=variant.product.slug)

    basket = _basket(request)
    basket[variant_id] = basket.get(variant_id, 0) + requested_quantity
    messages.success(request, "Added to basket.")
    request.session.modified = True

    return redirect("store:product_list")


def remove_from_basket(request, variant_id):
    """Remove a variant line entirely from the basket."""
    if request.method != "POST":
        return redirect("basket:view_basket")

    basket = _basket(request)
    key = str(variant_id)
    if key in basket:
        basket.pop(key)
        request.session.modified = True
    return redirect("basket:view_basket")


def view_basket(request):
    """Display the contents of the basket with item totals and grand total."""
    basket = _basket(request)
    variant_ids = [int(v_id) for v_id in basket.keys()]
    variants = {
        v.id: v for v in Variant.objects.filter(id__in=variant_ids)
    }

    items = []
    total = Decimal("0.00")

    for v_id_str, qty in basket.items():
        variant = variants.get(int(v_id_str))
        if not variant:
            continue

        line_total = variant.price * qty
        total += line_total

        items.append({
            "variant_id": variant.id,
            "name": str(variant),
            "qty": qty,
            "unit": variant.price,
            "line": line_total,
        })

    context = {"items": items, "total": total}
    return render(request, "basket/view_basket.html", context)


@require_POST
def empty(request):
    """Empty basket contents"""
    request.session.pop("basket", None)
    messages.success(request, "Your basket is now empty.")
    return redirect("basket:view_basket")


def update_quantity(request):
    """Update a basket item's quantity."""

    if request.method != "POST":
        return redirect("basket:view_basket")

    basket = _basket(request)

    try:
        v_id = str(int(request.POST.get("variant_id", "0")))
        qty = int(request.POST.get("qty", "1"))
    except ValueError:
        return redirect("basket:view_basket")

    if v_id not in basket:
        return redirect("basket:view_basket")

    if qty <= 0:
        basket.pop(v_id, None)
        request.session.modified = True
        return redirect("basket:view_basket")

    try:
        v = Variant.objects.select_related("stock").get(id=int(v_id))
        available = getattr(getattr(v, "stock", None), "quantity", None)
        if isinstance(available, int):
            qty = min(qty, max(0, available))
    except Variant.DoesNotExist:
        basket.pop(v_id, None)
        request.session.modified = True
        return redirect("basket:view_basket")

    basket[v_id] = qty
    request.session.modified = True
    return redirect("basket:view_basket")
