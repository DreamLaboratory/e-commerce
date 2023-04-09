# Register your models here.
from django.contrib import admin

from .models.order import Order

# TODO configure admin panel
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "order_number",
        "user",
        "get_full_name",
        "phone",
        "region",
        "cities",
        "address",
        "total_price",
        "ip",
        "status",
        "created_at",
    ]
    list_filter = ["status", "created_at", "updated_at"]
    search_fields = [
        "order_number",
        "user__username",
        "f_name",
        "l_name",
        "phone",
        "region__name",
        "cities__name",
        "address",
        "total_price",
        "ip",
        "status",
    ]
    list_per_page = 20
    date_hierarchy = "created_at"
    filter_horizontal = ["cart_items"]


admin.site.register(Order, OrderAdmin)
