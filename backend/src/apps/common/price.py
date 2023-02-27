from decimal import Decimal
from django.db.models import Sum, F

def prices(cart_items):
    cart_item = cart_items.annotate(price=F("product__price") * F("quantity"))
    total_price = cart_item.aggregate(total_price = Sum("price"))
    total_price = total_price["total_price"] or 0
    delevery = Decimal(total_price * Decimal(0.1)).quantize(Decimal("0.01"))
    grand_total = total_price + delevery

    return { 'total_price':total_price, 'delevery':delevery, 'grand_total': grand_total}