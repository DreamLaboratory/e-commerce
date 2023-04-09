import admin_thumbnails
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models.category import Category
from .models.product import Product, ProductImage
from .models.review import Review
from .models.variants import ProductVariants

# Register your models here.


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
        fields = "__all__"
        exclude = ("image",)


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource
    list_display = ("name", "slug", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    date_hierarchy = "created_at"


@admin_thumbnails.thumbnail("image")
class ProductImageModelAdmin(admin.TabularInline):
    model = ProductImage
    extra = 2


class ProductModelAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock", "category", "created_at")
    list_filter = ("category", "created_at")
    search_fields = ("name",)
    date_hierarchy = "created_at"
    list_editable = ("price", "stock")
    prepopulated_fields = {"slug": ("name",)}  # TODO - add slug field all models
    inlines = [ProductImageModelAdmin]


admin.site.register(Product, ProductModelAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("product", "user", "rating", "status", "created_at")
    list_filter = ("rating", "created_at")
    search_fields = ("user",)
    # autocomplete_fields = ("product",)
    raw_id_fields = ("user",)
    date_hierarchy = "created_at"
    list_editable = ("status",)


# admin.site.register(ProductImage)
admin.site.register(Review, ReviewAdmin)


class ProductVariantsAdmin(admin.ModelAdmin):
    list_display = ("product", "variant_category", "variant_value", "is_active", "created_at")
    list_filter = ("product", "created_at")
    search_fields = ("product",)
    date_hierarchy = "created_at"
    list_editable = ("is_active",)
    autocomplete_fields = ("product",)


admin.site.register(ProductVariants, ProductVariantsAdmin)
