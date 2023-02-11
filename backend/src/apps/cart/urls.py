from django.urls import path
from .views import add_cart, cart

urlpatterns = [
    path("", cart, name="cart"),
    path("add/cart/", add_cart, name="add_cart"),
]
