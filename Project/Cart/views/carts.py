from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, F
from django.db import models
from StoreApp.models.product import Product
from StoreApp.models.variants import ProductVariants
from ..models import Cart, CartItems, StatusChoices
from decimal import Decimal
from HomeApp.get_cart_id import cart_id


def carts(request):
    from HomeApp.alerter import tg_alert
    try:
        if request.user.is_authenticated:
            cart = Cart.objects.get(user=request.user)
        else:
            cart = Cart.objects.filter(cart_id=cart_id(request)).first()
            print(cart,'sedsdsd')

        cart_items = CartItems.objects.filter(cart=cart, status=StatusChoices.ACTIVE)
        if cart_items.count() != 0:
            total_price = cart_items.aggregate(
                total_price=Sum(
                    F("product__price") * F("quantity"),
                    output_field=models.DecimalField(max_digits=10, decimal_places=2)
                )
            )["total_price"]
            delevery = Decimal(total_price * Decimal(0.1)).quantize(Decimal("0.01"))  # 10% of total price
            grand_total = total_price + delevery
            context = {"cart_items": cart_items, "total_price": total_price, "delevery": delevery,
                       "grand_total": grand_total}
            return render(request, "store/cart_items.html", context)
        else:
            return render(request, "store/cart_items.html")

    except Exception as e:
        # tg_alert.custom_alert(f"{e}")
        print(e)
