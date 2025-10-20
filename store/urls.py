from django.urls import path
from . import views

app_name = "store"

urlpatterns = [
    path(
        "",
        views.product_list,
        name="product_list"
        ),
    path(
        "",
        views.product_list,
        name="home"
        ),
    path(
        "category/<slug:category_slug>/",
        views.product_list,
        name="category"
        ),
    path(
        "products/",
        views.product_list),
    path(
        "products/<slug:slug>/",
        views.product_detail,
        name="product_detail"
        ),
]
