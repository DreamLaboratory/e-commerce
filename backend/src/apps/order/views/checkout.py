from decimal import Decimal

from django.db.models import F, Sum
from django.shortcuts import render

from ...cart.models import Cart, CartItem, StatusChoices
from ...common.get_cart_id import _cart_id
from ..forms.order_form import OrderForm


def checkout(request):
    if request.user.is_authenticated:
        cart = Cart.objects.get(user=request.user)
    else:
        cart = Cart.objects.filter(cart_id_pk=_cart_id(request)).first()
    cart_items = CartItem.objects.filter(cart=cart, status=StatusChoices.ACTIVE)
    # annotate
    cart_item = cart_items.annotate(price=F("product__price") * F("quantity"))
    total_price = cart_item.aggregate(Sum("price"))
    total_price = total_price["price__sum"] or 0

    delevery_price = Decimal(total_price * Decimal(0.1)).quantize(Decimal("0.01"))  # 10% of total price

    grand_total = total_price + delevery_price
    form = OrderForm()
    context = {
        "cart_items": cart_items,
        "total_price": total_price,
        "delevery_price": delevery_price,
        "grand_total": grand_total,
        "form": form,
    }
    return render(request, "order/checkout.html", context)
