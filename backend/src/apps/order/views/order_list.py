from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models.order import Order


@login_required
def my_order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, "order/my_order_list.html", {"orders": orders})
