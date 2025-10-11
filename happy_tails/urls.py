from django.contrib import admin
from django.urls import path, include
from checkout import views as checkout_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("basket/", include("basket.urls")),
    path("checkout/", include("checkout.urls")),
    path("accounts/", include("allauth.urls")),
    path("", include(("store.urls", "store"), namespace="store")),
]
