from django.shortcuts import redirect, HttpResponse
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode
from django.contrib import messages


def activate(request, uidb64):
    try:
        User = get_user_model()
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(email=uid)
        user.is_active = True
        user.save(commit=True)
        messages.success(request, "Emailinggiz Muvafaqiyatli o'tkazildi")
        return redirect('accounts:signin')
    except:
        return redirect('accounts:register')
