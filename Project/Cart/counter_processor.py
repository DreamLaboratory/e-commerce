from .models import Cart, CartItems
from HomeApp.get_cart_id import cart_id
from django.db.models import Count
from django.shortcuts import redirect,render


def counter(request):
    try:
        if request.path.startswith("/admin"):
            return {}
        if request.user.is_authenticated:
            cart = Cart.objects.get(user=request.user)
        else:
            cart = Cart.objects.get(cart_id=cart_id(request))

        count = CartItems.objects.filter(cart=cart).count()
        return {"counter": count}

    except Exception as e:
        print(e)
        return {"counter": 0}

