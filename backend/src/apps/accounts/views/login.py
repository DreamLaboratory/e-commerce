from django.contrib import auth, messages
from django.shortcuts import render, redirect


def login(request):
    if request.user.is_authenticated:
        return redirect("accounts:index_page")
    if request.method != "POST":
        return render(request, "accounts/login.html")

    email = request.POST["email"]
    password = request.POST["password"]
    user = auth.authenticate(request, email=email, password=password)
    print(user)

    if user is not None:
        print("user is not None")
        auth.login(request, user)
        messages.success(request, "You are now logged in")
        return redirect("accounts:index_page")
    print("user is None")
    messages.error(request, "Invalid credentials")
    return redirect("accounts:login")
