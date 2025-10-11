from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("basket/", include("basket.urls")),
    path("accounts/", include("allauth.urls")),
    path("", include(("store.urls", "store"), namespace="store")),
]
