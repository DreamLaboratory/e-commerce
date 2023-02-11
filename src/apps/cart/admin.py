from django.contrib import admin


from .models import Cart, CartItem

class Cart(admin.ModelAdmin):
    list_display = 




admin.site.register(Cart)
admin.site.register(CartItem)
