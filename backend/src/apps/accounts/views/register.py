from ..forms.register_form import RegistrationForm
from django.shortcuts import render, redirect
from django.contrib import messages


def register(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_form = form.save()
            password = form.cleaned_data.get("password")
            new_form.set_password(password)
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            return redirect("accounts:login")
    return render(request, "accounts/register.html", {"form": form})
