from django.shortcuts import render, redirect
from .models import Cart, CartItem
from ..store.models.variant import ProductVariant
from django.db.models import Sum, F
from decimal import Decimal
from ..common.get_cart_id import _cart_id
from ..common.alert import tg_alert
from .choose import StatusChoices

# Create your views here.


def add_cart(request):
    if request.method != "POST":
        return render(request=request, template_name="product/cart_items.html")

    size = request.POST.get("size")
    color = request.POST.get("color")
    productid = request.POST.get("productid")

    cart, created = Cart.objects.get_or_create(cart_id_pk=_cart_id(request))
    variations = ProductVariant.objects.filter(product_id=productid, variant_value=[size, color])
    print("---1", cart)

    cart_items, created = CartItem.objects.get_or_create(cart=cart, product_id=productid)

    for variation in variations:
        cart_items.variants.add(variation)
    cart_items.save()

    return redirect("cart:cart")


def cart(request):
    cart = Cart.objects.filter(cart_id_pk=_cart_id(request)).first()
    cart_items = CartItem.objects.filter(cart=cart, status=StatusChoices.ACTIVE)
    # total_price = (
    #     cart_items.aggregate(
    #         total_price=Sum(
    #             F("product__price") * F("quantity"), out_fields=models.DecimalField(max_digits=10, decimal_places=2)
    #         )
    #     )["total_price"]
    #     or 0
    # )
    cart_item = cart_items.annotate(total_price=F("product__price") * F("quantity"))

    total_price = cart_item.aggregate(Sum("total_price"))
    total_price = total_price["total_price__sum"] or 0

    delevery = Decimal(total_price * Decimal(0.1).quantize(Decimal("0.01")))
    grand_total = total_price + delevery

    context = {
        "total_price": total_price,
        "delevery": delevery,
        "grand_total": grand_total,
        "cart_items": cart_items,
    }
    return render(request, template_name="product/cart_items.html", context=context)


def remove_cart(request, cart_items_id):
    try:

        cart_items = CartItem.objects.get(id=cart_items_id)
        cart_items.delete()
        return redirect("cart:cart")
    except Exception as e:

        tg_alert.custom_alert(f"Not id Cart in Cart Items {e}")
        return redirect("cart:cart")


def remove_cart_item(request, cart_item_id):
    try:
        cart_item = CartItem.objects.get(id=cart_item_id)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
        return redirect("cart:cart")
    except Exception:
        tg_alert.custom_alert(f"Don't exist cart item is ")


def add_cart_item(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect("cart:cart")
