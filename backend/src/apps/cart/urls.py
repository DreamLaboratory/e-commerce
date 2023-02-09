from django.urls import path
from .views import cart_items, add_cart

urlpatterns = [
    path("", cart_items, name="cart"),
    path("add/cart", add_cart, name="add_cart"),
]
