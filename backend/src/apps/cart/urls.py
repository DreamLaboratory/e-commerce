from django.urls import path

from .views import cart, add_cart

urlpatterns = [
    path("", cart, name="cart"),
    path("add/cart", add_cart, name="add_cart"),
]
