from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from profiles.models import Address
from store.models import Variant
import uuid
import stripe
from .models import Order, OrderItem
from django.conf import settings
from django.urls import reverse
from django.core.mail import send_mail

stripe.api_key = settings.STRIPE_SECRET_KEY


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
    user_profile = getattr(
        request.user, "profile", None
        )
    billing_default = (
         getattr(
            user_profile,
            "billing_address",
            None) if user_profile else None
        )
    delivery_default = (
        getattr(
            user_profile,
            "delivery_address",
            None) if user_profile else None
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
def create_order(request):
    """Start Stripe Checkout for the current basket."""
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
    variants = Variant.objects.filter(
        id__in=variant_ids
        ).select_related("product")

    line_items = []
    for variant in variants:
        quantity = int(basket[str(variant.id)])
        unit_amount = int(variant.price * 100)
        line_items.append({
            "price_data": {
                "currency": "gbp",
                "unit_amount": unit_amount,
                "product_data": {"name": f"{variant.product.name}".strip()},
            },
            "quantity": quantity,
        })

    request.session["checkout_addresses"] = {
        "billing_id": billing.id,
        "delivery_id": delivery.id,
    }
    request.session.modified = True

    success_url = request.build_absolute_uri(
        reverse("checkout:success")
    ) + "?session_id={CHECKOUT_SESSION_ID}"
    cancel_url = request.build_absolute_uri(reverse("checkout:start"))

    order_number = str(uuid.uuid4()).split("-")[0].upper()
    request.session["pending_order_number"] = order_number
    request.session.modified = True

    session = stripe.checkout.Session.create(
        mode="payment",
        line_items=line_items,
        success_url=success_url,
        cancel_url=cancel_url,
        client_reference_id=order_number,
        metadata={"user_id": str(
            request.user.id
            ), "order_number": order_number},
        payment_intent_data={"metadata": {"order_number": order_number}},
        )
    return redirect(session.url, permanent=False)


@login_required
def success(request):
    session_id = request.GET.get("session_id")

    if not session_id:
        return redirect("checkout:start")

    try:
        sess = stripe.checkout.Session.retrieve(session_id)
    except Exception:
        return redirect("checkout:start")

    order_number = (
        request.session.pop("pending_order_number", None)
        or getattr(sess, "client_reference_id", None)
        or (getattr(sess, "metadata", {}) or {}).get("order_number")
        )

    if getattr(sess, "payment_status", "") != "paid":
        return redirect("checkout:start")

    basket = request.session.get("basket", {})
    if not basket:
        return redirect("store:product_list")

    address_ids = request.session.get("checkout_addresses") or {}
    billing = get_object_or_404(
        Address, id=address_ids.get
        ("billing_id"), user=request.user)
    delivery = get_object_or_404(
        Address, id=address_ids.get
        ("delivery_id"), user=request.user)

    variant_ids = [int(k) for k in basket.keys()]
    variants = (
        Variant.objects
        .select_related("product")
        .filter(id__in=variant_ids)
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
        order_number=order_number or str(uuid.uuid4()).split("-")[0].upper(),
        paid=True,
        stripe_session_id=getattr(sess, "id", "")
    )

    for variant in variants:
        quantity = int(basket[str(variant.id)])
        OrderItem.objects.create(
            order=order,
            variant=variant,
            quantity=quantity,
            unit_price=variant.price,
        )

    request.session["basket"] = {}
    request.session.pop("checkout_addresses", None)
    request.session.modified = True

    if order.email:
        try:
            send_mail(
                f"Order {order.order_number} confirmation Email",
                (
                    f"Thanks you for ordering with Happy Tails!\n\n"
                    f"Order number: {order.order_number}\n"
                    f"Total: £{order.total}\n"
                ),
                settings.DEFAULT_FROM_EMAIL,
                [order.email],
                fail_silently=True,
            )
        except Exception:
            pass

    return render(request, "checkout/success.html", {"order": order})


@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by("-id")
    return render(request, "checkout/my_orders.html", {"orders": orders})
