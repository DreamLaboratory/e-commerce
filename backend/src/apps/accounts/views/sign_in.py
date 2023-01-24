from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render


def sign_in(request):
    if request.user.is_authenticated:
        return redirect("accounts:index_page")
    if request.method != "POST":
        return render(request, 'accounts/signin.html')

    email = request.POST["email"]
    password = request.POST["password"]
    if user := authenticate(request, email=email, password=password):
        login(request, user)
        messages.success(request, "You are now logged in")
        return redirect("accounts:index_page")
    messages.warning(request, "Invalid credentials")
    return redirect("accounts:sign_in")
