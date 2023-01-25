from django.shortcuts import render, redirect
from django.contrib import messages
from ..forms import UserForm
from django.db import transaction

from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail


def register(request):
    forms = UserForm()
    if request.method == "POST":
        forms = UserForm(request.POST)
        if forms.is_valid():
            email = request.POST['email']
            # forms.save(commit=False)
            forms.save(commit=True)
            subject = "Prime Team Jamoasidan"

            current_site = get_current_site(request)
            email_bytes = urlsafe_base64_encode(force_bytes(email))

            message = "Siz shu emaildan ro'yxatdan o'tyapsiz\n\n"
            message += f"https://{current_site.domain}/activate/{email_bytes}"
            to_email = request.POST['email']
            from_email = 'temurbekhamroyev41@gmail.com'

            send_mail(subject=subject, message=message,
                      from_email=from_email,  recipient_list=[to_email])
            # if send_mail:
            #     forms.save(commit=True)
            messages.warning(request, "Check Your Email !")
            return redirect("accounts:signin")
            # else:
            #     messages.warning(request, "Email is not EXIST")
            #     return redirect('accounts:register')
        else:
            return render(request, 'account/register.html', {'forms': forms})

    context = {'forms': forms}
    return render(request, 'account/register.html', context)
