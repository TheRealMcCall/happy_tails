from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile, Address
from .forms import ProfileForm


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


def profile_edit(request):
    """Page to edit profile"""
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profiles:profile")
    else:
        form = ProfileForm(instance=profile)
    return render(request, "profiles/profile_form.html", {"form": form})
