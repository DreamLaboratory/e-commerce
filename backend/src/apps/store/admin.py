from django.contrib import admin
from .models.product import Product
from .models.product import Category
from .models.review import Reviews
from .models.image import ImageProduct
from django.contrib import admin
from .models.variant import ProductVariant
import admin_thumbnails
from datetime import datetime
# Register your models here.
class CategoryModel(admin.ModelAdmin):
    list_display = ["name", "description", "image"]
    # prepopulated_fields = ['slug', ('name')]
admin.site.register(Category, CategoryModel)



class ReviewsModel(admin.ModelAdmin):
    list_display = ["user", "product", "status"]
    list_editable = ["status"]
admin.site.register(Reviews, ReviewsModel)



@admin_thumbnails.thumbnail('image')
class ImageProductModel(admin.TabularInline):
    model=ImageProduct
    extra=1


@admin.register(Product)
class ProductModel(admin.ModelAdmin):
    list_display=['category','name','image','is_availabel','stock']
    list_display_links=['category','image','name']
    list_editable=['is_availabel']
    # prepopulated_fields={('slug'):('name')}
    inlines=[ImageProductModel]
    

# TODO: amke AdminModel all model
#

class ProductVarisntsModel(admin.ModelAdmin):
    list_display = ["product", "variant_category", "variant_value", "is_active"]
    list_display_links = ["product", "variant_category"]
admin.site.register(ProductVariant, ProductVarisntsModel)







