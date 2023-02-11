from django.shortcuts import render, redirect
from .models import Cart, CartItem, StatusChoices
from ..store.models.variants import ProductVariants
from django.db.models import Sum, F
from django.db import models
from decimal import Decimal


def add_cart(request):
    """
    #TODO add to cart
    post:
        product id
        variations if
        quantity 1
    """
    # get product variations
    if request.method != "POST":
        return render(request, "store/cart_items.html", {"cart_items": None})
    product_id = request.POST.get("product_id")
    size = request.POST.get("size")
    color = request.POST.get("color")
    # check if cart exists
    cart, created = Cart.objects.get_or_create(user=request.user)

    variations = ProductVariants.objects.filter(product_id=product_id, variant_value__in=[size, color])
    print(variations)
    # check if cart item exists
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product_id=product_id)

    # add variations to cart item
    for variation in variations:
        cart_item.variations.add(variation)

    cart_item.save()

    return redirect("cart:cart")


def cart(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart, status=StatusChoices.ACTIVE)
    total_price = cart_items.aggregate(
        total_price=Sum(
            F("product__price") * F("quantity"), output_field=models.DecimalField(max_digits=10, decimal_places=2)
        )
    )["total_price"]
    delevery = Decimal(total_price * Decimal(0.1)).quantize(Decimal("0.01"))  # 10% of total price
    grand_total = total_price + delevery

    context = {"cart_items": cart_items, "total_price": total_price, "delevery": delevery, "grand_total": grand_total}
    return render(request, "store/cart_items.html", context)
