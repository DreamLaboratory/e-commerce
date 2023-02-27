from time import time

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from ...cart.models import CartItem
from ...common.cartstatus import CartStatus
from ...common.price import prices
from ...common.tg_alert import tg_alert
from ..forms.forms import OrderForm


@login_required(login_url='/signin')
def order_save(request):
    try:
        if request.POST:
            form = OrderForm(request.POST)
            if form.is_valid:
                order = form.save(commit=False)
                order.user = request.user
                cart_items = CartItem.objects.filter(cart__user = request.user, status = CartStatus.ACTIVE)
                order.order_number = str(int(time())) + str(request.user.id)
                order.total_price = prices(cart_items)['total_price']
                order.ip = request.META.get("REMOTE_ADDR")
                order.save()
                order.cart_items.set(cart_items)
                order.save()
                cart_items.update(status = CartStatus.INACTIVE)
                return redirect('order:order_list')
        return redirect('store:checkout')
    except Exception as e:
        tg_alert.custom_alert(f"Order app in errors", e)
        return redirect('order:checkout')