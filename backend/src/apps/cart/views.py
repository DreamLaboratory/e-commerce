from django.shortcuts import render, redirect
from .models import Cart, CartItem
from ..store.models.variant import ProductVariant
from django.db.models import Sum, F
from django.db import models
from decimal import Decimal

# Create your views here.


def add_cart(request):
    if request.method != "POST":
        return render(request=request, template_name="product/cart_items.html")

    size = request.POST.get("size")
    color = request.POST.get("color")
    productid = request.POST.get("productid")
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_items, created = CartItem.objects.get_or_create(cart=cart, product_id=productid)
    variations = ProductVariant.objects.filter(product_id=productid, variant_value=[size, color])

    for variation in variations:
        cart_items.variants.add(variation)
    cart_items.save()

    return redirect("cart:cart")


def cart(request):

    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    total_price = cart_items.aggregate(
        total_price=Sum(
            F("product__price") * F("quantity"), out_fields=models.DecimalField(max_digits=10, decimal_places=2)
        )
    )["total_price"]
    delevery = Decimal(total_price * Decimal(0.1).quantize(Decimal("0.01")))
    grand_total = total_price + delevery

    context = {
        "total_price": total_price,
        "delevery": delevery,
        "grand_total": grand_total,
        "cart_items": cart_items,
    }
    return render(request, template_name="product/cart_items.html", context=context)
