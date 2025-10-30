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
    path(
        "manage/products/<int:pk>/variants/new/",
        views.variant_create, name="variant_create"
        ),
    path(
        "manage/variants/choose/",
        views.variant_choose_product, name="variant_choose_product"
        ),
    path(
        "manage/variants/",
        views.manage_variants, name="manage_variants"
        ),
    path(
        "manage/variants/<int:pk>/edit/",
        views.variant_edit, name="variant_edit"
        ),
    path(
        "manage/variants/<int:pk>/stock/",
        views.variant_stock_update, name="variant_stock_update",
        ),
]
