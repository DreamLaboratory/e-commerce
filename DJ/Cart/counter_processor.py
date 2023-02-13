from .models import Cart, CartItems
from django.db.models import Count
from django.shortcuts import redirect,render


def counter(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
        if cart.count()!=0:
            cart = Cart.objects.get(user = request.user)
            count = CartItems.objects.filter(cart=cart).count()
            return {'counter':count}
    return {'counter':0}
