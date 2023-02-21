from django.contrib import admin

from .models.order import Order

# TODO configure admin panel
admin.site.register(Order)
