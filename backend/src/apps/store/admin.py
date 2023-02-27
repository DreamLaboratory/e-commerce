import admin_thumbnails
from django.contrib import admin
from django.db import models

from .models.category import Category
from .models.product import Product, Product_Image
from .models.review import Review
from .models.variants import ProductVariants

admin.site.register(Product_Image)
admin.site.register(Review)
admin.site.register(ProductVariants)

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


@admin_thumbnails.thumbnail('images')
class ProductImage(admin.TabularInline):
    model = Product_Image
    extra = 1


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity')
    list_filter = ('category', 'date_joined')
    list_editable = ('price' , 'quantity')
    search_fields = ('name',)
    prepopulated_fields = {'slug':('name',) }
    inlines = [ProductImage]
    # date_hierarchy= ('date_joined', )




