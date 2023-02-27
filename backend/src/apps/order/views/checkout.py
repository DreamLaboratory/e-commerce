from django.shortcuts import render
from django.db.models import F,Sum
from ...common.get_cart_id import _cart_id
from ...cart.models import CartItem,Cart
from decimal import Decimal
from ...cart.choose import StatusChoices
from ..forms.order_forms import OrderForm
from ...common.total_price import total_price_cart

def checkout(request):
    if request.user.is_authenticated:
        cart=Cart.objects.get(user=request.user)
    else:

        cart=Cart.objects.filter(cart_id_pk=_cart_id(request)).first()
    cart_items=CartItem.objects.filter(cart=cart,status=StatusChoices.ACTIVE)   
    total_price=total_price_cart(cart_items)
    delevery=Decimal(total_price*Decimal(0.1).quantize(Decimal('0.01')))
    grand_total=delevery+total_price
    
    form=OrderForm()
    context={
        'total_price':total_price,
        'delevery':delevery,
        'grand_total':grand_total,
        'form':form,
        'cart_items':cart_items
    }
    return render(request=request,template_name='order/checkout.html',context=context)
 
