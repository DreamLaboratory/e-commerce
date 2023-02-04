from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.image_product import ProductImage
from .models.review import Review



admin.site.register(Review)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductImage)
