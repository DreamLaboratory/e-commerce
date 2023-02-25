from django.shortcuts import render
from ..models.order import Order, OrderStatus
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def my_order_list(request):
    order_list = Order.objects.filter(user=request.user)
    return render(
        request,
        'order/order_list.html',
        context={'order_list': order_list}
    )
