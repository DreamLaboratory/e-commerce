from django.shortcuts import render, redirect
from django.contrib import messages
from ..forms import UserForm

from ...common.cart_item_id import _cart_id
from ...cart.models import Cart, CartItem
def register(request):
    forms = UserForm()
    if request.method == "POST":
        forms = UserForm(request.POST)
        if forms.is_valid():
            new_form = forms.save(commit=True)
            

            cart, created = Cart.objects.get_or_create(cart_id_pk = _cart_id(request))
            cart.user = new_form
            cart.save()

            messages.warning(request, "Check Your Email !")
            return redirect("accounts:signin")
        else:
            return render(request, 'account/register.html', {'forms': forms})

    context = {'forms': forms}
    return render(request, 'account/register.html', context)
