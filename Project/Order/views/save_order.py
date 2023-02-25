from ..forms.order_forms import OrderForm
from django.shortcuts import render, redirect
from Cart.models import Cart, CartItems, StatusChoices
from django.contrib.auth.decorators import login_required


from time import time
from django.db.models import F, Sum

@login_required(login_url='/login/')
def save_orders(request):
    if request.method == 'POST':
        form = OrderForm(request.POST);
        if form.is_valid():
            cart_items = CartItems.objects.filter(cart__user=request.user, status=StatusChoices.ACTIVE)
            total_price = cart_items.aggregate(total_price=Sum(F("product__price") * F("quantity")))["total_price"]
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.user = request.user
            order.order_number = str(int(time())) + str(request.user.id)
            order.total_price = total_price
            order.ip = request.META.get('REMOTE_ADDR')
            order.save()
            order.cart_items.set(cart_items)
            cart_items.update(status=StatusChoices.INACTIVE)
            order.save()
            return redirect('checkout')

    return redirect('checkout')