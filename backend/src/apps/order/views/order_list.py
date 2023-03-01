from django.shortcuts import render, redirect
from ...common.tg_alert import tg_alert
from ..models import Order


from django.contrib.auth.decorators import login_required

@login_required(login_url='/signin/')
def order_list(request):
    order = Order.objects.filter(user = request.user)
    return render(request, 'order/dashboard.html', {'orders':order})
