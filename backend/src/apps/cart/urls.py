from django.urls import path
from .views import cart, add_cart, remove_cartitem, plus_cart, minus_cart

urlpatterns = [
    path('cart/', cart, name='cart'),
    path('cart/add', add_cart, name='add_cart'),
    path('remove/<int:cart_item_id>', remove_cartitem, name='remove_cart'),
    path('add/<int:cart_item_id>', plus_cart, name='plus_cart'),
    path('removed/<int:cart_item_id>', minus_cart, name='minus_cart'),

]
