from ..forms.register_form import RegistrationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site

from django.core.mail import EmailMessage
from django.utils.html import strip_tags
from django.db import transaction

from django.utils.http import urlsafe_base64_encode


@transaction.atomic
def register(request):
    try:
        form = RegistrationForm()
        if request.method == "POST":
            form = RegistrationForm(request.POST)
            if form.is_valid():
                with transaction.atomic():
                    new_form = form.save(commit=False)
                    password = form.cleaned_data.get("password")
                    new_form.set_password(password)
                    new_form.save()
                    # send email to user
                    email = form.cleaned_data.get("email")
                    username = form.cleaned_data.get("username")
                    firstname = form.cleaned_data.get("firstname")

                    current_site = get_current_site(request)
                    domain = f"http://{current_site.domain}/activate/{urlsafe_base64_encode(force_bytes(new_form))}/"
                    subject = "Welcome to the site"
                    message = f"Hi {firstname}, welcome to the site"
                    body = render_to_string(
                        "accounts/verification.html",
                        {
                            "subject": subject,
                            "body": message,
                            "domain": domain,
                        },
                    )
                    html_body = strip_tags(body)
                    sendmail = EmailMessage(
                        subject=subject,
                        body=html_body,
                        to=[email],
                    )
                    sendmail.send()

                messages.success(request, f"Account created for {username}!")
                return redirect("accounts:login")
        return render(request, "accounts/register.html", {"form": form})
    except Exception as e:
        messages.error(request, f"Error: {e}")
        return redirect("accounts:register")
