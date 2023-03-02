from ..forms.order_forms import OrderForm
from time import time
from ...cart.models import CartItem
from ...cart.choose import StatusChoices
from django.shortcuts import redirect
from ...common.total_price import total_price_cart
from django.contrib.auth.decorators import login_required


@login_required()
def save_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                print('-----',request.user)
                order.user = request.user
            cart_items = CartItem.objects.filter(cart__user=request.user, status=StatusChoices.ACTIVE)
            total_price = total_price_cart(cart_items)
            order = form.save(commit=False)
            order.total_price = total_price
            order.order_number = str(time()) + str(request.user.id)
            order.ip = request.META.get("REMOTE_ADDR")
            order.save()

            order.cart_items.set(cart_items)  # ikkala usul xam birxil
            # for cart_item in cart_items:
            #     order.cart_items.add(cart_item.id)
            cart_items.update(status=StatusChoices.INACTIVE)
            order.save()

            return redirect("order:checkout")

    return redirect("order:checkout")
