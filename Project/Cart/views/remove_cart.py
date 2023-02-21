from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, F
from django.db import models
from StoreApp.models.product import Product
from StoreApp.models.variants import ProductVariants
from ..models import Cart, CartItems, StatusChoices
from decimal import Decimal



def remove_cart(request, id):
    menus = request.POST.get('menus')
    plus = request.POST.get('plus')
    cart_items = CartItems.objects.get(id=id).delete()
    return redirect('carts')


def menus_cart(request, id):
    from HomeApp.alerter import tg_alert
    try:
        cart_item = CartItems.objects.get(id=id)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except Exception as e:
        tg_alert.custom_alert(f"{e}")
    return redirect('carts')