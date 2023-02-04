from django.contrib import admin
from .models.product import Product
from .models.product import Category
from .models.review import Reviews

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
# admin.site.register(Reviews)
