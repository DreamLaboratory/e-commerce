from django.shortcuts import render, redirect
from .models import Cart, CartItem, StatusChoices
from ..store.models.variants import ProductVariants
from django.db.models import Sum, F
from django.db import models
from decimal import Decimal
from ..common.get_cart_id import _cart_id


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
    cart, created = Cart.objects.get_or_create(cart_id_pk=_cart_id(request))
    print('cart', cart)
    variations = ProductVariants.objects.filter(product_id=product_id, variant_value__in=[size, color])
    print(variations)
    # check if cart item exists
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product_id=product_id)

    # add variations to cart item
    for variation in variations:
        cart_item.variations.add(variation)

    cart_item.save()

    return redirect("cart:cart")


def add_to_cart(request, cart_item_id):
    """
    TODO: Optimize this function
    """
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.quantity += 1
    cart_item.save()

    return redirect("cart:cart")

def cart(request):
    cart = Cart.objects.filter(cart_id_pk=_cart_id(request)).first()
    cart_items = CartItem.objects.filter(cart=cart, status=StatusChoices.ACTIVE)
    cart_item = cart_items.annotate(total_price=F("product__price") * F("quantity"))
    total_price = cart_item.aggregate(Sum("total_price"))
    print(total_price)
    total_price = total_price["total_price__sum"] or 0

    delevery = Decimal(total_price * Decimal(0.1)).quantize(Decimal("0.01"))  # 10% of total price

    grand_total = total_price + delevery

    context = {"cart_items": cart_items, "total_price": total_price, "delevery": delevery, "grand_total": grand_total}
    return render(request, "store/cart_items.html", context)


def delete_cart(request, cart_item_id):
    # TODO use get_object_or_404
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.delete()
    return redirect("cart:cart")


def remove_cart_item(request, cart_item_id):
    try:
        # TODO use get_object_or_404
        cart_item = CartItem.objects.get(id=cart_item_id)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except Exception:
        # TODO tg alert
        pass
    return redirect("cart:cart")