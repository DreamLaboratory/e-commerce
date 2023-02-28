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
from HomeApp.sms_sender import SendSMS


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


def send_sms_after(request, phone_number):
    user_account = Profile.objects.get(phone_number=phone_number)
    current_site = get_current_site(request)
    print(phone_number)
    print(urlsafe_base64_encode(force_bytes(user_account)))
    message = f"You accounts need to be verified !\n" \
              f"http://{current_site.domain}/verify/{urlsafe_base64_encode(force_bytes(user_account))}/"
    sms = SendSMS()
    sms.send_sms(phone_number,message)



def verify(request, auth_token):
    print('as')
    if request.method == "GET":
        try:
            uid = urlsafe_base64_decode(auth_token).decode()
            user = get_object_or_404(Profile, phone_number=uid)
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


def send_reset_password(request, phone_number):
    user_account = Account.objects.get(phone_number=phone_number)
    print(user_account)
    current_sent = get_current_site(request)
    message = f"" \
              f"You accounts need to be verified !\n" \
              f"Hi paste the link to reset password : " \
              f" http://{current_sent.domain}/reset_password/{urlsafe_base64_encode(force_bytes(user_account))}"
    sms = SendSMS()
    sms.send_sms(phone_number,message)
