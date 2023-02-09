from django.shortcuts import render
from .models import Cart, CartItems
from asyncio.log import logger
from django.contrib.auth import get_user_model
from StoreApp.models.product import Product
from StoreApp.models.variants import ProductVariants
from .models import Cart,CartItems

def cart_items(request):
    try:
        cart, create = Cart.objects.get_or_create(user=request.user)
        cart_item = CartItems.objects.filter(cart=cart)
        return render(request, 'store/cart_items.html', {"cart_items": cart_item})

    except Exception as e:
        logger.error(e)
        return render(request, 'store/cart_items.html', {"cart_items": None})


def add_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id',None)
        color = request.POST.get('color',None)
        size = request.POST.get('size',None)
        product = Product.objects.get(id = product_id)

    return render(request, 'store/cart_items.html', {"cart_items": None})
