from django.contrib import admin
from .models import (
    Category,
    Product,
    Variant,
    Stock,
    ProductImage,
    ProductReview,
    Wishlist
    )


class ProductImageInline(admin.StackedInline):
    """Inline for managing product images within the product admin."""
    model = ProductImage
    extra = 1
    fields = ("image",
              "alt_text",
              "is_thumbnail"
              )
    show_change_link = True


class VariantInline(admin.StackedInline):
    """Inline for managing product variants within the product admin."""
    model = Variant
    extra = 1
    fields = ("sku",
              "size",
              "colour",
              "price",
              "is_available"
              )
    show_change_link = True


class StockInline(admin.StackedInline):
    """Inline for managing stock within the variant admin."""
    model = Stock
    extra = 0
    min_num = 0
    max_num = 1
    can_delete = True


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin configuration for product categories."""
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)
    list_display = ("name",)
    ordering = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin configuration for products, with variant and image inlines."""
    list_display = ("name",
                    "category",
                    "is_available",
                    "created_on"
                    )
    list_filter = ("category",
                   "is_available"
                   )
    search_fields = ("name",
                     "slug",
                     "category__name",
                     "variants__sku"
                     )
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ("created_on",)
    autocomplete_fields = ("category", "image")
    inlines = [VariantInline, ProductImageInline,]
    list_select_related = ("category",)


@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    """Admin configuration for product variants with stock inline."""
    list_display = ("product",
                    "sku",
                    "size",
                    "colour",
                    "price",
                    "is_available"
                    )
    list_filter = ("is_available",
                   "product__category",
                   "size",
                   "colour"
                   )
    search_fields = ("sku",
                     "product__name"
                     )
    autocomplete_fields = ("product",)
    inlines = [StockInline]
    list_select_related = ("product",
                           "product__category"
                           )


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    """Admin configuration for product images."""
    list_display = ("__str__",
                    "product",
                    "variant",
                    "is_thumbnail",
                    "created_on"
                    )
    list_filter = ("is_thumbnail",
                   "created_on",
                   "product"
                   )
    search_fields = ("alt_text",
                     "product__name",
                     "variant__sku"
                     )
    autocomplete_fields = ("product",
                           "variant"
                           )


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    """Admin configuration for product reviews."""
    list_display = ("product",
                    "user",
                    "rating",
                    "created_at"
                    )
    list_filter = ("rating",
                   "created_at"
                   )
    search_fields = ("product__name",
                     "user__username",
                     "comment"
                     )
    autocomplete_fields = ("product",
                           "user"
                           )


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    """Admin configuration for user wishlists."""
    list_display = ("user",)
    search_fields = ("user__username",
                     "user__email"
                     )
    filter_horizontal = ("products",)
