from django.urls import path
from .views import add_cart,remove_cart,carts




urlpatterns = [
    path('add-cart/', add_cart.add_cart, name='add_cart'),
    path('carts/',carts.carts,name = 'carts'),
    path('remove_cart/<int:id>',remove_cart.remove_cart,name = 'remove_cart'),
    path('cart_remove/<int:id>/', remove_cart.menus_cart, name='cart_item_menus'),
    path('cart_add/<int:id>/', add_cart.plus_cart, name='cart_item_plus'),
]


