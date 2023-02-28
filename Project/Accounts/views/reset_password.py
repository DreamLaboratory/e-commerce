from django.contrib import messages
from django.shortcuts import render, redirect
from ..forms import RegistrationForm
from ..models import Account, Profile
import uuid
from .token_send_mail import send_reset_password
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode
from django.shortcuts import get_object_or_404


def forget_password(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number', None)
        user = Account.objects.filter(phone_number=phone_number)
        if user:
            send_reset_password(request, phone_number)
            return redirect('token')
        else:
            messages.error(request, "Phone Number Not Found!")
    return render(
        request,
        'accounts/email_form.html'
    )


# 904271974
def reset_password(request, uidb64):
    if request.method == "POST":
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        if password == password1:
            User = get_user_model()
            print(User)
            uid = urlsafe_base64_decode(uidb64).decode()
            print(uid)
            user = get_object_or_404(User, phone_number=uid)
            user.set_password(password)
            user.save()
            messages.success(request, "Password reset successfully")
            return redirect("login")
        else:
            messages.error(request, "Passwords do not match")
    return render(
        request,
        'accounts/reset_password_form.html'
    )
