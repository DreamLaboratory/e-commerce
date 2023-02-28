from django.contrib import messages
from django.shortcuts import render, redirect
from ..forms import RegistrationForm
from ..models import Account, Profile
from HomeApp.alerter import tg_alert
from .token_send_mail import send_mail_after,send_sms_after
from django.db import transaction
from Cart.models import Cart, CartItems
from HomeApp.get_cart_id import cart_id


@transaction.atomic
def register_view(request):
    try:
        if request.method == 'POST':
            form = RegistrationForm(request.POST or None)
            if form.is_valid():
                new_form = form.save(commit=False)
                email = form.cleaned_data.get('email')
                phone_number = form.cleaned_data.get('phone_number')
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                new_form.set_password(password)
                new_form.save()
                user = Account.objects.get(email=email)
                profile_obj = Profile.objects.create(
                    user=user,
                    email=email,
                    username=username,
                    phone_number=phone_number,
                )
                profile_obj.save()
                # Email send
                # send_mail_after(request, email)
                # Send SMS
                send_sms_after(request,phone_number)

                cart, created = Cart.objects.get_or_create(cart_id=cart_id(request))
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
        print(e)
        return redirect('login')


