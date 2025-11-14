from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from store.models import Variant
from django.contrib import messages
from django.views.decorators.http import require_POST


def _basket(request):
    """Return the session basket, creating it if missing."""
    return request.session.setdefault("basket", {})


@require_POST
def add_to_basket(request):
    """Add a variant to the session basket and redirect to the basket view."""
    try:
        variant_id = int(request.POST.get("variant", "0"))
    except (TypeError, ValueError):
        messages.error(request, "invalid product selection.")
        return redirect("store:product_list")

    try:
        requested_quantity = max(1, int(request.POST.get("qty", "1")))
    except ValueError:
        requested_quantity = 1

    variant = get_object_or_404(
        Variant.objects.select_related("stock", "product"),
        pk=variant_id,
    )

    available_quantity = int(
        getattr(getattr(variant, "stock", None), "quantity", 0) or 0
        )

    if available_quantity <= 0:
        messages.error(request, "Sorry, this item is out of stock.")
        return redirect("store:product_detail", slug=variant.product.slug)

    basket = _basket(request)
    key = str(variant.id)
    current_quantity = int(basket.get(key, 0))

    if current_quantity + requested_quantity > available_quantity:
        if current_quantity >= available_quantity:
            messages.error(
                request, f"Sorry, only {available_quantity} in stock."
                )
        else:
            remaining = available_quantity - current_quantity
            messages.error(
                request, f"Only {remaining} more are in stock."
                )
        return redirect("store:product_detail", slug=variant.product.slug)

    basket[key] = current_quantity + requested_quantity
    request.session.modified = True
    messages.success(request, "Added to basket.")
    return redirect("store:product_list")


@require_POST
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

        product_name = variant.product.name
        size = (getattr(variant, "size", "") or "").strip()
        colour = (getattr(variant, "colour", "") or "").strip()
        variant_options = " / ".join(
            opt for opt in (size, colour) if opt
        )

        if variant_options:
            display_name = f"{product_name} ({variant_options})"
        else:
            display_name = product_name

        photo = variant.product.get_product_image()

        items.append({
            "variant_id": variant.id,
            "name": display_name,
            "qty": qty,
            "unit": variant.price,
            "line": line_total,
            "image_url": photo.image.url if photo else None
        })

    context = {"items": items, "total": total}
    return render(request, "basket/view_basket.html", context)


@require_POST
def empty(request):
    """Empty basket contents"""
    request.session.pop("basket", None)
    messages.success(request, "Your basket is now empty.")
    return redirect("basket:view_basket")


@require_POST
def update_quantity(request):
    """Update a basket item's quantity."""
    basket = _basket(request)

    try:
        variant_id = int(request.POST.get("variant_id", "0"))
        qty = int(request.POST.get("qty", "1"))
    except (TypeError, ValueError):
        messages.error(request, "Invalid quantity.")
        return redirect("basket:view_basket")

    v_id = str(variant_id)
    if v_id not in basket:
        messages.error(request, "Item not found in basket.")
        return redirect("basket:view_basket")

    if qty <= 0:
        basket.pop(v_id, None)
        request.session.modified = True
        messages.success(request, "Item removed from basket.")
        return redirect("basket:view_basket")

    try:
        v = Variant.objects.select_related("stock").get(id=variant_id)
    except Variant.DoesNotExist:
        basket.pop(v_id, None)
        request.session.modified = True
        messages.error(
            request, "That item is no longer available.")
        return redirect("basket:view_basket")

    available = getattr(getattr(v, "stock", None), "quantity", None)
    if isinstance(available, int):
        if available <= 0:
            messages.error(
                request, "This item is out of stock.")
            return redirect("basket:view_basket")
        if qty > available:
            qty = available
            messages.warning(
                request, f"Quantity adjusted to available stock ({available})."
                )

    basket[v_id] = qty
    request.session.modified = True
    messages.success(request, "Quantity updated.")
    return redirect("basket:view_basket")
