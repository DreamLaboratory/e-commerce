from django.contrib import messages
from django.shortcuts import render,redirect
from ..forms import RegistrationForm
from ..models import Account,Profile
import uuid
from .token_send_mail import send_mail_after





def register_view(request):
    form = RegistrationForm()
    if request.method=='POST':
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_form = form.save(commit=False)
            password = form.cleaned_data.get('password')
            new_form.set_password(password)
            new_form.save()
            email = form.cleaned_data.get('email')
            profile_obj = Profile.objects.create(
                email = email
            )
            profile_obj.save()

            ###Email send
            send_mail_after(request,email)
            return redirect('token')
    else:
        form = RegistrationForm()
    return render(
        request,
        'accounts/register.html',
        context={'form':form}
    )
