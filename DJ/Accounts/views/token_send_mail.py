from django.shortcuts import render,redirect
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from ..models import Profile,Account
from django.utils.http import urlsafe_base64_decode
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
def token_view(request):
    return render(
        request,
        'parts/send.html'
    )


def send_mail_after(email,token):
    subject = 'You accounts need to be verified !'
    message = F"Hi paste the link to verify your account :  http://127.0.0.1:8000/verify/{token}"
    email_form = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,message,email_form,recipient_list)




def verify(request,auth_token):
    try:
        profile_obj = Profile.objects.get(auth_token=auth_token)
        if profile_obj:
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request,'Your email has been verified.')
            return redirect('login')
        else:
            return redirect('error')
    except Exception as e:
        print(e)
        return redirect('login')


def error_page(request):
    return render(
        request,
        'parts/error.html'
    )


def send_reset_password(request,email):
    user_account = Account.objects.get(email=email)
    current_sent = get_current_site(request)
    subject = 'You accounts need to be verified !'
    message = f"Hi paste the link to reset password :  http://{current_sent.domain}/reset_password/{urlsafe_base64_encode(force_bytes(user_account))}"
    email_form = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,message,email_form,recipient_list)

