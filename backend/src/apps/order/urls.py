from django.urls import path
from .views.checkout import checkout
from .views.order_save import order_save
from .views.order_list import order_list


urlpatterns = [

    path('check/', checkout, name='checkout'),
    path('save/', order_save, name='order_save'),
    path('list/', order_list, name='order_list'),

]