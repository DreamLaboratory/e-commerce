from django.contrib import auth, messages
from django.shortcuts import render, redirect
from ...cart.models import Cart
from ...common.get_cart_id import _cart_id


def login(request):
    if request.user.is_authenticated:
        return redirect("accounts:index_page")

    if request.method != "POST":
        return render(request, "accounts/login.html")

    email = request.POST["email"]
    password = request.POST["password"]
    if user := auth.authenticate(request, email=email, password=password):
        auth.login(request, user)

        # TODO filter by session key
        cart, _ = Cart.objects.get_or_create(cart_id_pk=_cart_id(request))
        cart.user = user
        cart.save()

        messages.success(request, "You are now logged in")
        return redirect("accounts:index_page")
    messages.warning(request, "Invalid credentials")
    return redirect("accounts:login")
