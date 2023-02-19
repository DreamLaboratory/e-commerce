from .views import add_cart, cart, remove_cart
from django.urls import path

urlpatterns = [
    path("", cart, name="cart"),
    path("add/cart/", add_cart, name="add_cart"),
    path("remove/<int:cart_items_id>/", remove_cart, name="remove_cart"),
]
