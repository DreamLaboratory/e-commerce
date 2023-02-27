from ..models.order import Order
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def my_order_list(request):
    orders=Order.objects.filter(user=request.user)
    context={
        'orders':orders
    }
    return render(request=request,template_name='order/order_list.html',context=context)