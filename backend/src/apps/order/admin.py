# Register your models her
from django.contrib import admin
from .models.order import Order

#
@admin.register(Order)
class OrderModeladmin(admin.ModelAdmin):
    list_display=['order_number','user','phone','status','region']
    list_display_links=['order_number','user']
    list_editable=['status']
    
