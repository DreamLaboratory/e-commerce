from .models import Cart, CartItem
from ..common.cart_item_id import _cart_id
from ..common.cartstatus import CartStatus

def counter(request):
    try: 
        if request.user.is_authenticated:
            cart = Cart.objects.get(user=request.user)
        else:
            cart = Cart.objects.get(cart_id_pk = _cart_id(request))
        cart_item = CartItem.objects.filter(cart=cart, status = CartStatus.ACTIVE)

        counter = cart_item.count()

        return {'counter':counter}
    except Cart.DoesNotExist:
        return {'counter': 0}
