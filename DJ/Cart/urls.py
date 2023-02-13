from django.urls import path
from .views import add_cart,carts

urlpatterns = [

    path('add-cart/', add_cart, name='add_cart'),
    path('carts/',carts,name = 'carts')
]
