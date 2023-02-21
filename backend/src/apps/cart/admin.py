from django.contrib import admin

# Register your models here.
from .models import Cart, CartItem

# TODO: Add more admin details
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("id", "cart", "product", "quantity", "status")
    filter_horizontal = ("variations",)


admin.site.register(Cart)
admin.site.register(CartItem, CartItemAdmin)
