from django.contrib import admin
from .models.category import Category
from .models.product import Product, ProductImage
from .models.review import Review

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)


#
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("product", "user", "rating", "status", "created_at")
    list_filter = ("rating", "created_at")
    list_display_links = ("product", "user")
    raw_id_fields = ("user",)
    search_fields = ["product", "user"]
    # autocomplete_fields = ["product"]
    date_hierarchy = "created_at"
    list_editable = ("status",)


admin.site.register(Review, ReviewAdmin)
