from django.urls import path
from .views.checkout import checkout
urlpatterns = [
    path('checkout/',checkout,name='checkout'),
]