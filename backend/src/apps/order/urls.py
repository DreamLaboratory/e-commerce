from django.urls import path

from .views.checkout import checkout
from .views.save_order import save_orders
from .views.order_list import my_order_list

urlpatterns = [
    path("checkout/", checkout, name="checkout"),
    path("save/", save_orders, name="save_order"),
    path("list/", my_order_list, name="order_list"),
]
