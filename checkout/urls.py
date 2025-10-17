from django.urls import path
from . import views

app_name = "checkout"

urlpatterns = [
    path("", views.checkout_view, name="start"),
    path("create/", views.create_order, name="create"),
    path("success/", views.success, name="success"),
]
