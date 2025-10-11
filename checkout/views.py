from django.shortcuts import render


def checkout_view(request):
    return render(request, "checkout/checkout.html")
