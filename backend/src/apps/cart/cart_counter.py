from .models import Cart, CartItem
from django.db.models import Sum


def processor_cart_count(request):
    if request.user.is_authenticated:
        user, created = Cart.objects.get_or_create(user=request.user)
        counter = CartItem.objects.filter(cart=user).aggregate(counter=Sum("quantity"))
        return counter
    else:
        return {"counter": 0}
