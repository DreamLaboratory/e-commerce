from .views import add_cart, cart
from django.urls import path

urlpatterns = [
    path("", cart, name="cart"),
    path("add/cart/", add_cart, name="add_cart"),
]
