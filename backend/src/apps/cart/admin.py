from django.contrib import admin

# Register your models here.fr
from .models import Cart, CartItem

# TODO: Add more admin details
admin.site.register(Cart)
admin.site.register(CartItem)
