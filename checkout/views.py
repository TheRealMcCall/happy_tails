from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from profiles.models import Address
from store.models import Variant, Stock
import uuid
from .models import Order, OrderItem
from django.db import transaction


def _basket(request):
    return request.session.setdefault("basket", {})


@login_required
def checkout_view(request):
    basket = _basket(request)
    if not basket:
        return redirect("basket:view_basket")

    variant_ids = [int(k) for k in basket.keys()]
    variants = {
        variant.id: variant
        for variant in Variant.objects.filter(
            id__in=variant_ids
            ).select_related("product")
    }
    items = []
    subtotal = Decimal("0.00")

    for variant_id_str, quantity in basket.items():
        variant = variants.get(int(variant_id_str))
        if not variant:
            continue
        line = variant.price * quantity
        subtotal += line
        items.append({
            "variant_id": variant.id,
            "name": f"{variant.product.name} - "
                    f"{(getattr(variant, 'name', '') or '').strip()}",
            "qty": quantity,
            "unit_price": variant.price,
            "line_total": line,
        })

    addresses = Address.objects.filter(user=request.user).order_by("id")
    profile = getattr(
        request.user, "profile", None
        )
    billing_default = (
         getattr(profile, "billing_address", None) if profile else None
        )
    delivery_default = (
        getattr(profile, "delivery_address", None) if profile else None
        )

    if not billing_default:
        billing_default = addresses.first()
    if not delivery_default:
        delivery_default = addresses.first()

    context = {
        "items": items,
        "sub_total": subtotal,
        "total": subtotal,
        "addresses": addresses,
        "billing_default": billing_default,
        "delivery_default": delivery_default,
    }
    return render(request, "checkout/checkout.html", context)


@login_required
@transaction.atomic
def create_order(request):
    """Create an order from the current basket and clear the basket."""
    if request.method != "POST":
        return redirect("checkout:start")

    basket = request.session.get("basket", {})
    if not basket:
        return redirect("basket:view_basket")

    billing_id = request.POST.get("billing_address_id")
    delivery_id = request.POST.get("delivery_address_id")
    if not billing_id or not delivery_id:
        return redirect("checkout:start")

    billing = get_object_or_404(Address, id=billing_id, user=request.user)
    delivery = get_object_or_404(Address, id=delivery_id, user=request.user)

    variant_ids = [int(k) for k in basket.keys()]
    variants = (
        Variant.objects
        .select_for_update()
        .filter(id__in=variant_ids)
        .select_related("product",)
        )

    subtotal = Decimal("0.00")
    for variant in variants:
        quantity = int(basket[str(variant.id)])
        subtotal += variant.price * quantity

    order = Order.objects.create(
        user=request.user,
        billing_address=billing,
        delivery_address=delivery,
        sub_total=subtotal,
        total=subtotal,
        email=request.user.email or "",
        order_number=str(uuid.uuid4()).split("-")[0].upper(),
    )

    for variant in variants:
        quantity = int(basket[str(variant.id)])
        OrderItem.objects.create(
            order=order,
            variant=variant,
            quantity=quantity,
            unit_price=variant.price,
        )

        stock, _ = Stock.objects.select_for_update().get_or_create(
            variant=variant,
            defaults={"quantity": 0},
            )
        if stock.quantity < quantity:
            raise ValueError(
                f"Insufficient stock for {variant} "
                f"(have {stock.quantity}, need {quantity})"
                )
        stock.quantity -= quantity
        stock.save(update_fields=["quantity"])

    request.session["basket"] = {}
    request.session.modified = True

    return redirect("checkout:success", order_number=order.order_number)


@login_required
def success(request, order_number):
    order = get_object_or_404(
        Order,
        order_number=order_number,
        user=request.user
        )

    return render(request, "checkout/success.html", {"order": order})
