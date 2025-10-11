from decimal import Decimal
from django.shortcuts import render, redirect
from store.models import Variant


def _basket(request):
    return request.session.setdefault("basket", {})


def add_to_basket(request):
    """Add a variant to the session basket and redirect to the basket view."""
    v_id = request.POST.get("variant_id")

    if not v_id:
        return redirect("store:product_list")

    basket = _basket(request)
    basket[v_id] = basket.get(v_id, 0) + 1
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
            "name": str(variant),
            "qty": qty,
            "unit": variant.price,
            "line": line_total,
        })

    context = {"items": items, "total": total}
    return render(request, "basket/view_basket.html", context)
