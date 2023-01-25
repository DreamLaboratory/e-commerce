from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate
from django.contrib import messages


def Login(request):
    if request.user.is_authenticated:
        return redirect('accounts:index_page')

    if request.method != 'POST':
        return render(request, 'account/signin.html')

    email = request.POST['email']
    password = request.POST['password']

    user = authenticate(request, email=email, password=password)
    if user := authenticate(request, email=email, password=password):
        login(request, user)
        messages.success(request, "Tabriklaymiz siz Login qildinggiz")
        return redirect('accounts:index_page')
    else:
        messages.warning(request, "Email or Password incorrect")
        return render(request, 'account/signin.html', {'email': email})
