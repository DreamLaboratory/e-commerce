from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.image_product import ProductImage
from .models.review import Review
from .models.variants import ProductVariants
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("product", "user", "rating", "status", "created_at")
    list_filter = ("rating", "created_at")
    search_fields = ("user",)

    raw_id_fields = ("user",)
    date_hierarchy = "created_at"
    list_editable = ("status",)




admin.site.register(Review, ReviewAdmin)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductImage)
admin.site.register(ProductVariants)

