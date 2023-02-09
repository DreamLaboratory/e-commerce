from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from ..models import Profile, Account
from django.utils.http import urlsafe_base64_decode
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.shortcuts import get_object_or_404

def token_view(request):
    return render(
        request,
        'parts/send.html'
    )


def send_mail_after(request, email):
    user_account = Profile.objects.get(email=email)
    current_sent = get_current_site(request)
    subject = 'You accounts need to be verified !'
    message = f"Hi paste the link to reset password :  http://{current_sent.domain}/verify/{urlsafe_base64_encode(force_bytes(user_account))}"
    email_form = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_form, recipient_list)


def verify(request,auth_token):
    if request.method == "GET":
        try:
            uid = urlsafe_base64_decode(auth_token).decode()
            user = get_object_or_404(Profile,email=uid)
            if user:
                user.is_verified = True
                user.save()
                messages.success(request, 'Your email has been verified.')
                return redirect('login')
            else:
                return redirect('error')
        except Exception as e:
            messages.success(request, 'Xatolik yuz berdi')
            return redirect('login')
    return redirect('login')

def error_page(request):
    return render(
        request,
        'parts/error.html'
    )


def send_reset_password(request, email):
    user_account = Account.objects.get(email=email)
    current_sent = get_current_site(request)
    subject = 'You accounts need to be verified !'
    message = f"Hi paste the link to reset password :  http://{current_sent.domain}/reset_password/{urlsafe_base64_encode(force_bytes(user_account))}"
    email_form = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_form, recipient_list)
