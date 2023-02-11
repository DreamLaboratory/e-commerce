from django.contrib import admin

from .models import Cart, CartItem

# TODO: Add more admin details
admin.site.register(Cart)
admin.site.register(CartItem)
