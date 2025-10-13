from decimal import Decimal
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from profiles.models import Address
from store.models import Variant


def _basket(request):
    return request.session.setdefault("basket", {})


@login_required
def checkout_view(request):
    basket = _basket(request)
    if not basket:
        return redirect("basket:view_basket")

    ids = [int(k) for k in basket.keys()]
    variants = {v.id: v for v in Variant.objects.filter(id__in=ids).select_related("product")}
    items = []
    sub_total = Decimal("0.00")

    for v_id_str, qty in basket.items():
        v = variants.get(int(v_id_str))
        if not v:
            continue
        line = v.price * qty
        sub_total += line
        items.append({
            "variant_id": v.id,
            "name": f"{v.product.name} — {(getattr(v, 'name', '') or '').strip()}",
            "qty": qty,
            "unit_price": v.price,
            "line_total": line,
        })

    addresses = Address.objects.filter(user=request.user).order_by("id")
    profile = getattr(
        request.user, "profile", None
        )
    billing_default = getattr(profile, "billing_address", None) if profile else None
    delivery_default = getattr(profile, "delivery_address", None) if profile else None

    if not billing_default:
        billing_default = addresses.first()
    if not delivery_default:
        delivery_default = addresses.first()

    context = {
        "items": items,
        "sub_total": sub_total,
        "total": sub_total,
        "addresses": addresses,
        "billing_default": billing_default,
        "delivery_default": delivery_default,
    }
    return render(request, "checkout/checkout.html", context)
