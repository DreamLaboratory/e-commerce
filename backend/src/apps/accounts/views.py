from ..common.get_cart_id import _cart_id
from ..cart.models import Cart
from django.shortcuts import render, redirect
from .forms.forms import RegisterForm
from django.contrib import messages
from django.contrib import auth
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.db import transaction
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib.sites.shortcuts import get_current_site
from .models import MyUser
from ..common.sender import SendSMS

# Create your views here.


def index(request):

    return render(request=request, template_name="index.html")


@transaction.atomic
def register(request):
    try:
        forms = RegisterForm()
        if request.method == "POST":
            forms = RegisterForm(request.POST)
            if forms.is_valid():
                with transaction.atomic():
                    new_forms = forms.save(commit=False)
                    password = forms.cleaned_data.get("password")
                    username = forms.cleaned_data.get("first_name")
                    phone_number = forms.cleaned_data.get("phone_number")
                    forms.cleaned_data.get("email")

                    new_forms.set_password(password)
                    new_forms.username = username
                    new_forms.save()
                    # how to send sms message
                    sms = SendSMS()

                    # TODO: emailga borishiga saqlanishni qilish
                    uuid = urlsafe_base64_encode(force_bytes(new_forms))
                    current_site = get_current_site(request=request)
                    domain = f"http://{current_site.domain}/activate/{uuid}/"
                    subject = "Welcome to site"
                    message = f"HI {username}, welcome to site"
                    body = render_to_string(
                        ["register/verification.html"],
                        {
                            "subject": subject,
                            "message": message,
                            "uuid": uuid,
                            "domain": domain,
                        },
                    )
                    print(phone_number)

                    html_body = strip_tags(body)
                    result = sms.send_sms(phone_number, html_body)
                    print(result)

                    # cart_id create
                    cart, _ = Cart.objects.get_or_create(cart_id_pk=_cart_id(request))
                    cart.user = new_forms
                    cart.save()

                messages.success(request, f"User created for {username}")
                return redirect("accounts:redirect_login")
        return render(request=request, template_name="register/register.html", context={"forms": forms})
    except Exception as e:
        messages.error(request, f"error {e}")
        return redirect("accounts:register")


def login(request):

    if request.method == "POST":
        phone_number = request.POST.get("phone_number")
        password = request.POST.get("password")
        user = auth.authenticate(request, phone_number=phone_number, password=password)
        if user:
            auth.login(request, user)
            messages.success(request, "You are soccessed login")
            return redirect("accounts:index")
        else:
            return HttpResponse("Login Failed")
    return render(request, "register/login.html")


def logout(request):
    auth.logout(request)
    return redirect("accounts:login")


def auth_email(request):

    if request.method == "POST":
        email = request.POST.get("email")
        # user=auth.authenticate(request=request,email=email)
        user = MyUser.objects.filter(email=email).exists()
        if user:
            subject = "Please click below url"
            current_site = get_current_site(request=request)
            uuid = urlsafe_base64_encode(force_bytes(email))
            domain = f"http://{current_site.domain}/forgot_password/{uuid}/"

            context_message = render_to_string(
                "register/verifiy_email.html",
                {
                    "subject": subject,
                    "domain": domain,
                },
            )
            body = strip_tags(context_message)
            sendmail = EmailMessage(subject=subject, body=body, to=[email])
            sendmail.send()
            messages.success(request, "Pleasce check your email")
            return redirect("accounts:redirect_login")
    return render(request=request, template_name="register/auth_email.html")


def forgot_password(request, uidb64):
    try:
        if request.method == "POST":
            password = request.POST.get("password")
            confirm_password = request.POST.get("confirm_password")
            if password == confirm_password:
                decode_email = force_text(urlsafe_base64_decode(uidb64))
                user = MyUser.objects.get(email=decode_email)
                user.set_password(password)
                user.save()
                return redirect("accounts:login")
    except Exception as ex:
        return ex

    return render(request=request, template_name="register/forgot.html")


def redirect_login(request):

    return render(request=request, template_name="register/redirect_login.html")
