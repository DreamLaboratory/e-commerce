from django.shortcuts import render, redirect
from ...common.tg_alert import tg_alert
from ..models import Order


def order_list(request):
    try:
        order = Order.objects.filter(user = request.user)
        return render(request, 'order/dashboard.html', {'orders':order})
    except Exception as e:
        tg_alert.custom_alert(e)
        return redirect('order:order_list')