from django.urls import path
from ..order.views.order import order_view

urlpatterns = [
    path("", order_view, name="order"),
]
