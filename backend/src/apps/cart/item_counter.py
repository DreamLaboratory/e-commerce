from .models import Cart, CartItem


def counter(request):
    # TODO cache
    try:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        counter = cart_items.count()
        # TODO user  Sum aggregation
        return {"counter": counter}
    except:
        return {"counter": 0}
