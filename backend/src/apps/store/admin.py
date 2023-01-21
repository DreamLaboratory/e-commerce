from django.contrib import admin

# Register your models here.

from .models.product import Product
from .models.category import Category

admin.site.register(Product)
admin.site.register(Category)
