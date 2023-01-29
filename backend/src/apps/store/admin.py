from django.contrib import admin
from .models.product import Product
from .models.product import Category

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
