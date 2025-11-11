from decimal import Decimal
from store.models import Variant


def basket_summary(request):
    """Render basket total summary"""
    ZERO = Decimal("0.00")
    session_basket = request.session.get("basket", {})

    quantities_by_variant_id = {}
    for variant_key, stored_value in session_basket.items():
        try:
            variant_id = int(variant_key)
        except (TypeError, ValueError):
            continue

        if isinstance(stored_value, int):
            quantity = max(0, stored_value)
        elif isinstance(stored_value, dict):
            try:
                quantity = max(0, int(stored_value.get("qty", 0)))
            except (TypeError, ValueError):
                quantity = 0
        else:
            quantity = 0

        if quantity:
            quantities_by_variant_id[variant_id] = (
                quantities_by_variant_id.get(variant_id, 0) + quantity
            )

    if not quantities_by_variant_id:
        return {"basket_total": ZERO}

    prices_by_variant_id = dict(
        Variant.objects.filter(
            id__in=quantities_by_variant_id
            ).values_list("id", "price")
    )

    basket_total = sum(
        prices_by_variant_id.get(variant_id, ZERO) * quantity
        for variant_id, quantity in quantities_by_variant_id.items()
    )
    return {"basket_total": basket_total}
