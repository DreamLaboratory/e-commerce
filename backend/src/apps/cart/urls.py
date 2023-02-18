from django.urls import path

from .views import cart, add_cart
from .views import cart, add_cart, delete_cart, remove_cart_item, add_to_cart

urlpatterns = [
    path("", cart, name="cart"),
    path("add/cart", add_cart, name="add_cart"),
    path("delete/<int:cart_item_id>", delete_cart, name="delete_cart"),
    path("remove/<int:cart_item_id>", remove_cart_item, name="remove_cart_item"),
    path("add/<int:cart_item_id>", add_to_cart, name="add_to_cart"),
]
