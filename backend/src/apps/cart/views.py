from asyncio.log import logger

from django.shortcuts import render
from .models import Cart, CartItem

# list all cart items


def cart_items(request):
    try:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        return render(request, "store/cart_items.html", {"cart_items": cart_items})
    except Exception as e:
        logger.error(e)
        return render(request, "store/cart_items.html", {"cart_items": None})


def add_cart(request):
    """
    #TODO add to cart
    post:
        product id
        variations if {list}
        quantity 1
    """
    # get product variations
    if request.method == "POST":
        for item in request.POST:
            print(item)

    return render(request, "store/cart_items.html", {"cart_items": None})
