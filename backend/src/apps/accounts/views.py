from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib import auth
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.db import transaction
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site

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
                    new_forms.set_password(password)
                    new_forms.save()

                    # how to send email message
                    uuid = urlsafe_base64_encode(force_bytes(new_forms))
                    username = forms.cleaned_data.get("username")
                    to_email = forms.cleaned_data.get("email")
                    current_site = get_current_site(request=request)
                    domain = f"http://{current_site.domain}/activate/{uuid}/"
                    subject = "Welcome to site"
                    message = f"HI {username}, welcome to site"
                    context_message = render_to_string(
                        ["register/verification.html"],
                        {
                            "subject": subject,
                            "message": message,
                            "uuid": uuid,
                            "domain": domain,
                        },
                    )

                    body = strip_tags(context_message)
                    sendmail = EmailMessage(
                        subject=subject,
                        body=body,
                        to=[to_email],
                    )
                    sendmail.send()
                messages.success(request, f"User created for {username}")
                return redirect("accounts:login")
        return render(request=request, template_name="register/register.html", context={"forms": forms})
    except Exception as e:
        messages.error(request, f"error {e}")
        return redirect("accounts:register")


def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = auth.authenticate(request, email=email, password=password)
        if user:
            auth.login(request, user)
            messages.success(request, "You are soccessed login")
            return redirect("accounts:index")
        else:
            return HttpResponse("Login Failed")
    return render(request, "register/login.html")
