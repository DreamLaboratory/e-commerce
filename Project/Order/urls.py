from django.urls import path
from .views.checkout import checkout
from .views.save_order import save_orders
from .views.order_list import my_order_list
urlpatterns = [
    path('checkout/',checkout,name='checkout'),
    path('order-save/',save_orders,name = 'order_save'),
    path('order-list/',my_order_list,name='order_list'),
]