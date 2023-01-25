from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from django.core.mail import send_mail

from ..models import User

from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model


def forgotpassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            subject = "This Message for Reset Password"
            current_site = get_current_site(request)
            uidb64 = urlsafe_base64_encode(force_bytes(email))
            message = "Password ni tiklash uchun ushbu urlga kiring\n\n"
            message += f"http://{current_site.domain}/resetpassword/{uidb64}"
            from_email = 'temurbekhamroyev41@gmail.com'
            send_mail(subject=subject, message=message,
                      from_email=from_email, recipient_list=[email])
            messages.success(request, "Check Your Email")
            return redirect('accounts:signin')

        messages.warning(request, "Email is not Exist")
        return redirect('accounts:register')
    return render(request, 'account/verifyemail.html')


def resetpass(request, uidb64):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            User = get_user_model()
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(email=uid)
            print('User ', user)
            user.set_password(password)
            user.save()
            messages.success(request, "Your Password has been updated")
            return redirect('accounts:signin')
        messages.warning(
            request, "Password and Confirm Password are not equal")
        return redirect('accounts:resetpassword')
    return render(request, "account/verify_password.html")
