from django.urls import path
from . import views

app_name = "checkout"

urlpatterns = [

    path(
        "",
        views.checkout_view,
        name="start"
        ),

    path(
        "create/",
        views.create_order,
        name="create"
        ),

    path(
        "success/",
        views.success,
        name="success"
        ),

    path(
        "my-orders/",
        views.my_orders,
        name="my_orders"
        ),

    path(
        "orders/<str:order_number>/",
        views.order_detail,
        name="order_detail"
        ),
]
