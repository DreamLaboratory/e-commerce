from .views import cart_item, add_cart
from django.urls import path

urlpatterns = [
    path("", cart_item, name="cart_item"),
    path("add/cart", add_cart, name="add_cart"),
]
