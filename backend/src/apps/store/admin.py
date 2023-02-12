from django.contrib import admin
from .models.product import Product
from .models.product import Category
from .models.review import Reviews
from .models.image import ImageProduct
from django.contrib import admin
from .models.variant import ProductVariant


# Register your models here.
admin.site.register(Product)
admin.site.register(Category)


class ReviewsModel(admin.ModelAdmin):
    list_display = ["user", "product", "status"]
    list_editable = ["status"]


admin.site.register(Reviews, ReviewsModel)


class ImageProductModel(admin.ModelAdmin):
    list_display = ["product", "image"]
    list_display_links = ["product"]
    list_editable = ["image"]
    raw_id_fields = ["product"]


admin.site.register(ImageProduct, ImageProductModel)


# TODO: amke AdminModel all model
#
class ProductVarisntsModel(admin.ModelAdmin):
    list_display = ["product", "variant_category", "variant_value", "is_active"]
    list_display_links = ["product", "variant_category"]


admin.site.register(ProductVariant, ProductVarisntsModel)
