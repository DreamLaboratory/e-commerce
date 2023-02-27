from django.urls import path
from .views.checkout import checkout
from .views.save_order import save_order
from .views.order_list import my_order_list

urlpatterns = [
    path("checkout/", checkout, name="checkout"),
    path("save-order/", save_order, name="save_order"),
    path('list/',my_order_list,name='my_order_list')
]
