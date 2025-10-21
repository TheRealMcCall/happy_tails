from django.urls import path
from . import views

app_name = "profiles"

urlpatterns = [
    path("", views.profile, name="profile"),
    path("edit/", views.profile_edit, name="profile_edit"),

    path("addresses/add/", views.address_add, name="address_add"),
    path("addresses/<int:pk>/edit/", views.address_edit, name="address_edit"),
    path("addresses/<int:pk>/delete/", views.address_delete, name="address_delete"),
]
