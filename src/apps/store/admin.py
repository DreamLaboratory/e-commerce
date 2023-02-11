from django.contrib import admin

# Register your models here.

from .models.product import Product
from .models.category import Category
from .models.review import Review
from .models.product import ProductImage
from .models.variants import ProductVariants


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("product", "user", "rating", "status", "created_at")
    list_filter = ("rating", "created_at")
    search_fields = ("user",)
    # autocomplete_fields = ("product",)
    raw_id_fields = ("user",)
    date_hierarchy = "created_at"
    list_editable = ("status",)
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "description", "price")
    list_filter = ("category",)
    search_fields = ("name",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "description", "created_at")
    list_filter = ("name",)
    search_fields = ("name",)



class ProductVariantsAdmin(admin.ModelAdmin):
    list_display = ("product", "variant_category", "variant_value", "is_active")
    list_filter = ("product",)
    list_editable = ("is_active",)


admin.site.register(ProductImage)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductVariants, ProductVariantsAdmin)
