from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, F
from django.db import models
from HomeApp.get_cart_id import cart_id
from StoreApp.models.product import Product
from StoreApp.models.variants import ProductVariants
from ..models import Cart, CartItems, StatusChoices
from decimal import Decimal


def add_cart(request):
    if request.method != 'POST':
        return render(request, 'store/cart_items.html', {"cart_items": None})

    product_id = request.POST.get('product_id', None)
    color = request.POST.get('color', None)
    size = request.POST.get('size', None)
    variations = ProductVariants.objects.filter(product_id=product_id, variant_value__in=[size, color])
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        cart, created = Cart.objects.get_or_create(cart_id=cart_id(request))

    cart_item, created = CartItems.objects.get_or_create(cart=cart, product_id=product_id)
    print(variations)

    for variation in variations:
        cart_item.variants.add(variation)

    cart_item.save()
    return redirect('carts')


def plus_cart(request, id):
    from HomeApp.alerter import tg_alert
    try:
        cart_item = CartItems.objects.get(id=id)
        cart_item.quantity += 1
        cart_item.save()
    except Exception as e:
        tg_alert.custom_alert(f"{e}")
    return redirect('carts')
