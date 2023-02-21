from .views import add_cart, cart, remove_cart, remove_cart_item, add_cart_item
from django.urls import path

urlpatterns = [
    path("", cart, name="cart"),
    path("add/cart/", add_cart, name="add_cart"),
    path("remove/<int:cart_items_id>/", remove_cart, name="remove_cart"),
    path("remove_item/<int:cart_item_id>", remove_cart_item, name="remove_cart_item"),
    path("add_item/<int:cart_item_id>", add_cart_item, name="add_cart_item"),
]
