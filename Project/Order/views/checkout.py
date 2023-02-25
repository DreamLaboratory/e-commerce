from django.shortcuts import render
from HomeApp.models import BaseModel
from Cart.models import Cart, CartItems, StatusChoices
from decimal import Decimal
from HomeApp.get_cart_id import cart_id
from django.db.models import F, Sum
from ..forms.order_forms import OrderForm


def checkout(request):
    total = 0
    if request.user.is_authenticated:
        cart = Cart.objects.get(user=request.user)
    else:
        cart = Cart.objects.filter(cart_id=cart_id(request)).first()
    cart_items = CartItems.objects.filter(cart=cart, status=StatusChoices.ACTIVE)

    # annotate
    price = cart_items.annotate(price=F("product__price") * F("quantity"))
    total_price = price.aggregate(Sum("price"))
    total_price = total_price['price__sum'] or 0
    delevery = Decimal(total_price * Decimal(0.1)).quantize(Decimal("0.01"))  # 10% of total price
    form = OrderForm()
    grand_total = total_price + delevery
    context = {"cart_items": cart_items,
               "total_price": total_price,
               "delevery": delevery,
               "grand_total": grand_total,
               'form': form}
    return render(request, "order/checkout.html", context)