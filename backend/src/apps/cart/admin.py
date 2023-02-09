from django.contrib import admin

# Register your models here.
from .models import Cart, CartItem

# TODO: Add more admin details
admin.site.register(Cart)
admin.site.register(CartItem)
