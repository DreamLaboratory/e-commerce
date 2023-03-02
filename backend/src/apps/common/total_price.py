from django.db.models import F, Sum


def total_price_cart(cart_items):
    cart_item = cart_items.annotate(total_price=F("product__price") * F("quantity"))
    total_price = cart_item.aggregate(Sum("total_price"))
    total_price = total_price["total_price__sum"] or 0
    return total_price
