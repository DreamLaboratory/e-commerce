from django.shortcuts import render
from .models import Cart, CartItem
from asyncio.log import logger

# Create your views here.


def cart_item(request):
    try:

        cart, created = Cart.objects.get_or_create()
        cartitems = CartItem.objects.filter(cart=cart)
        return render(request=request, template_name="product/cart_items.html")
    except Exception as e:
        logger.error(e)
        return render(request, "product/cart_items.html", {"cart_items": None})


def add_cart(request):
    print("----1", request.POST())
    return render(request, template_name="product/cart_items")
