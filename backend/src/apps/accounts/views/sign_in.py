from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from ..forms.sign_in_form import SignInForm


def sign_in(request):
    if request.user.is_authenticated:
        return redirect("accounts:index_page")
    if request.method != "POST":
        form = SignInForm()
        return render(request, 'accounts/signin.html', {"form": form})

    form = SignInForm(request=request, data=request.POST)
    if form.is_valid():
        user = authenticate(
            email=form.cleaned_data["username"],
            password=form.cleaned_data["password"],
        )
        if user is not None:
            login(request, user)
            messages.success(request, f"Hello {user.username}! You have been logged in")
            return redirect("/")

    else:
        for key, error in list(form.errors.items()):
            if key == 'captcha' and error[0] == 'This field is required.':
                messages.error(request, "You must pass the reCAPTCHA test")
                continue

            messages.error(request, error)
