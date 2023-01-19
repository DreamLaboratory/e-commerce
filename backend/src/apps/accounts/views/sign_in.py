from django.contrib import messages
from django.shortcuts import redirect, render

from ..forms.register_form import RegistrationForm


def sign_in(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login/')
        else:
            form = RegistrationForm()
            messages.error(request, f'Error!')
            return render(request, 'accounts/register.html', {'form': form})
    else:
        form = RegistrationForm()
        return render(request, 'accounts/register.html', {'form': form})
