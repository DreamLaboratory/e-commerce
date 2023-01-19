from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render

from ..forms.register_form import RegistrationForm
from .tokens import account_activation_token

from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage


def activate(request, uuidb64, token):
    User = get_user_model()
    try:
        uuid = force_str(urlsafe_base64_decode(uuidb64))
        user = User.objects.get(pk=uuid)
    except:
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success((request, "Thank you for your email confirmation. Now you can login your account."))
        return redirect('/sign_in/')
    else:
        messages.error(request, "Actication link is invalid!")
    return redirect("/")


def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string("template_activate_account.html", {
        "user": user.username,
        "domain": get_current_site(request).domain,
        "uuid": urlsafe_base64_encode(force_bytes(user.pk)),
        "token": account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user}<b>. Go {to_email}')
    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('/sign-in/')
        else:
            form = RegistrationForm()
            print("else")
            messages.error(request, f'Error!')
            return render(request, 'accounts/register.html', {'form': form})
    else:
        print("method : ", request.method)
        form = RegistrationForm()
        return render(request, 'accounts/register.html', {'form': form})
