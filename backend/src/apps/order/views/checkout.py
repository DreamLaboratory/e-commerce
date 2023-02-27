from django.shortcuts import render

from ...cart.models import Cart, CartItem
from ...common.cart_item_id import _cart_id
from ...common.cartstatus import CartStatus
from ...common.price import prices
from ..forms.forms import OrderForm


def checkout(request):
    if request.user.is_authenticated:
        cart = Cart.objects.get(user = request.user)
    else:
        cart = Cart.objects.get(cart_id_pk=_cart_id(request))
    cart_items = CartItem.objects.filter(cart=cart, status = CartStatus.ACTIVE)
    price = prices(cart_items)
    form = OrderForm()

    context = {'cart_items':cart_items, 'form':form, 'total_price':price['total_price'], 'delevery': price['delevery'], 'grand_total':price['grand_total']}

    return render(request, 'order/checkout.html', context)  






