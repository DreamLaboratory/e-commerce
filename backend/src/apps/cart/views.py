from asyncio.log import logger
from decimal import Decimal

from django.db.models import F, Sum
from django.shortcuts import get_object_or_404, redirect, render

from ..common.cart_item_id import _cart_id
from ..common.cartstatus import CartStatus
from ..common.tg_alert import tg_alert
from ..store.models.variants import ProductVariants
from .models import Cart, CartItem
from ..common.price import prices

def add_cart(request):
    try:
        if request.method != "POST":
            return render(request, 'store/cart.html')
        
        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user)
        else:
            cart, created = Cart.objects.get_or_create(cart_id_pk = _cart_id(request))
        print(_cart_id(request))

        product_id = request.POST['product']
        color = request.POST['color']
        size = request.POST['size']
    
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product_id=product_id)

        variants = ProductVariants.objects.filter(product_id=product_id, value__in=[color,size] )
        for variant in variants:
            cart_item.variation.add(variant)
        cart_item.save()
        
        return redirect('cart:cart')
    
    except Exception as e:
        tg_alert.custom_alert(e)


def cart(request):
    try:
        if request.user.is_authenticated:
            cart = Cart.objects.get(user=request.user)
        else:
            cart = Cart.objects.filter(cart_id_pk=_cart_id(request)).first()
        
        cart_items = CartItem.objects.filter(cart=cart, status=CartStatus.ACTIVE)
        price = prices(cart_items)

        context = {'cart_items':cart_items, 'total_price':price['total_price'], 'delevery': price['delevery'], 'grand_total':price['grand_total']}

        return render(request, 'store/cart.html', context)
    
    except Exception as e:
        logger.error(e)
        tg_alert.custom_alert(e)
        return render(request, 'store/cart.html', {'cart_items' : 0} )


def remove_cartitem(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.delete()

    return redirect('cart:cart')


def plus_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(id = cart_item_id)
    quantity = cart_item.quantity
    quantity += 1
    cart_item.quantity= quantity
    cart_item.save()
    return redirect('cart:cart')


def minus_cart(request, cart_item_id):
    try:
        cart_item = CartItem.objects.get(id = cart_item_id)

        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except Exception as e:
        tg_alert.custom_alert(f"Errors in cart models",{e})

    return redirect('cart:cart')

    


