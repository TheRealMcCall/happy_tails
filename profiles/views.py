from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Profile, Address


@login_required
def profile(request):
    """Render the profile page"""
    prof = get_object_or_404(Profile, user=request.user)
    addresses = Address.objects.filter(user=request.user).order_by("id")
    return render(
        request,
        "profiles/profile.html",
        {"profile": prof, "addresses": addresses},
    )
