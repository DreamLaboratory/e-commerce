from django.urls import path

from .views.checkout import checkout
from .views.save_order import save_orders

urlpatterns = [
    path("checkout/", checkout, name="checkout"),
    path("save_order/", save_orders, name="save_order"),
]
