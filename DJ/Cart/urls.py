from django.urls import path
from .views import cart_items,add_cart


urlpatterns = [
    path(
        'cart/', cart_items, name='cart_items',
    ),
    path('add/cart', add_cart, name='add_cart')
]


