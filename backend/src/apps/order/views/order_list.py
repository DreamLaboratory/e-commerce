from django.shortcuts import render

from ..models import Order


def order_list(request):
    order = Order.objects.filter(user = request.user)
    return render(request, 'order/dashboard.html', {'orders':order})
