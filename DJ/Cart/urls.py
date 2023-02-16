from django.urls import path
from .views import add_cart,carts,remove_cart


urlpatterns = [
    path('add-cart/', add_cart, name='add_cart'),
    path('carts/',carts,name = 'carts'),
    path('remove_cart/<int:id>',remove_cart,name = 'remove_cart'),

]
