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

    path(
        "manage/catalog/",
        views.manage_dashboard,
        name="manage_dashboard"
        ),
    path(
        "manage/products/new/",
        views.product_create, name="product_create"
        ),
    path(
        "manage/products/<int:pk>/edit/",
        views.product_edit, name="product_edit"
        ),
    path(
        "manage/products/<int:pk>/delete/",
        views.product_delete, name="product_delete"
        ),
]
