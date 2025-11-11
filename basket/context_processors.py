def basket_summary(request):
    """Return basket item count."""
    session_basket = request.session.get("basket", {})

    count = 0
    for stored_value in session_basket.values():
        if isinstance(stored_value, int):
            count += max(0, stored_value)
        elif isinstance(stored_value, dict):
            try:
                count += max(0, int(stored_value.get("qty", 0)))
            except (TypeError, ValueError):
                continue

    return {"basket_total": count}
