# logout
from django.contrib.auth import logout
from django.shortcuts import redirect


def logout_user(request):
    logout(request)
    return redirect("accounts:index_page")
