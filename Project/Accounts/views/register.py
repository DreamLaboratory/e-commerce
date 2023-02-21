from django.contrib import messages
from django.shortcuts import render, redirect
from ..forms import RegistrationForm
from ..models import Account, Profile
from HomeApp.alerter import tg_alert
import asyncio
from .token_send_mail import send_mail_after
from django.db import transaction
from Cart.models import Cart,CartItems
from HomeApp.get_cart_id import cart_id


@transaction.atomic
def register_view(request):
    try:
                form = RegistrationForm()
                if request.method == 'POST':
                    form = RegistrationForm(request.POST or None)
                    if form.is_valid():
                        new_form = form.save(commit=False)
                        password = form.cleaned_data.get('password')
                        new_form.set_password(password)
                        new_form.save()
                        email = form.cleaned_data.get('email')
                        profile_obj = Profile.objects.create(
                            email=email


                        )
                        profile_obj.save()
                        ###Email send

                        send_mail_after(request, email)
                        print(cart_id(request))
                        cart,created = Cart.objects.get_or_create(cart_id=cart_id(request))
                        cart.user = new_form
                        cart.save()
                        return redirect('token')
                else:
                    form = RegistrationForm()
                return render(
                    request,
                    'accounts/register.html',
                    context={'form': form}
                )
    except Exception as e:
        tg_alert.custom_alert(f"{e}")
