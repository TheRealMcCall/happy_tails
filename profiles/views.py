from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile, Address
from .forms import ProfileForm, AddressForm
from checkout.models import Order
from django.contrib import messages


@login_required
def profile(request):
    """Render the profile page."""
    profile = get_object_or_404(Profile, user=request.user)
    addresses = Address.objects.filter(user=request.user).order_by("id")
    recent_orders = (
        Order.objects.filter(user=request.user)
        .order_by("-created_at", "-id")[:5]
    )
    return render(
        request,
        "profiles/profile.html",
        {
         "profile": profile,
         "addresses": addresses,
         "recent_orders": recent_orders
        },
    )


@login_required
def profile_edit(request):
    """Page to edit profile."""
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile has been updated.")
            return redirect("profiles:profile")
    else:
        form = ProfileForm(instance=profile)

    return render(
        request,
        "profiles/profile_form.html",
        {"form": form},
    )


@login_required
def address_add(request):
    """Create a new address for the current user."""
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            messages.success(request, "Address has been added.")
            return redirect("profiles:profile")
    else:
        form = AddressForm()

    return render(
        request,
        "profiles/address_form.html",
        {"form": form, "title": "Add address"},
    )


@login_required
def address_edit(request, pk):
    """Edit a users existing address."""
    addr = get_object_or_404(Address, pk=pk, user=request.user)
    if request.method == "POST":
        form = AddressForm(request.POST, instance=addr)
        if form.is_valid():
            form.save()
            messages.success(request, "Address has been updated.")
            return redirect("profiles:profile")
    else:
        form = AddressForm(instance=addr)

    return render(
        request,
        "profiles/address_form.html",
        {"form": form, "title": "Edit address"},
    )


@login_required
def address_delete(request, pk):
    """Delete a users existing address."""
    address = get_object_or_404(Address, pk=pk, user=request.user)
    if request.method == "POST":
        address.delete()
        messages.success(request, "Address has been deleted.")
        return redirect("profiles:profile")

    return render(
        request,
        "profiles/address_delete.html",
        {"address": address},
    )
