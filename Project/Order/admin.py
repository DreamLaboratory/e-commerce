from django.contrib import admin
from .models.order import Order,OrderStatus
from import_export import resources
from import_export.admin import ImportExportModelAdmin
class OrderResource(resources.ModelResource):
    class Meta:
        model = Order
        fields = ('order_number', 'user', 'f_name', 'l_name', 'phone', 'cart_items')


@admin.register(Order)
class OrderModelAdmin(ImportExportModelAdmin):
    resource_class = OrderResource
    list_display = ('user', 'order_number', 'total_price','status')
    list_display_links = ('user', 'order_number')
    list_filter = ('user',)
    list_editable = ('status',)
    search_fields = ('order_number',)
    date_hierarchy = "created_at"

    def status_canceled(self,request,queryset):
        queryset.update(status = OrderStatus.CANCELED)

    short_description = 'All items canceled'
    actions = ['status_canceled']

