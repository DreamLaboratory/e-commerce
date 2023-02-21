from django.contrib import admin
from .models import Cart, CartItems,StatusChoices
from django.contrib.auth.admin import UserAdmin


class CartAdmin(admin.ModelAdmin):
    list_display = ('user','created_at','updated_at')
    list_display_links = ('user','created_at','updated_at')


class CartItemsAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('cart','product','quantity','status')
    list_display_links = ('cart','product')

    def default_status_active(self,request,queryset):
        queryset.update(status = StatusChoices.ACTIVE)
    default_status_active.short_description = 'Default status Active'

    def default_status_inactive(self,request,queryset):
        queryset.update(status = StatusChoices.INACTIVE)

    default_status_inactive.short_description = "Default status inactive"

    actions = ['default_status_active','default_status_inactive']


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItems,CartItemsAdmin)
