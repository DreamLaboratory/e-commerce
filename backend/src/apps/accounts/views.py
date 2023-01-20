from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import UserForm

from django.core.mail import send_mail

# Create your views here.


class IndexView(TemplateView):
    template_name = "index.html"


index_page = IndexView.as_view()


def Login(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Tabriklaymiz siz Login qildinggiz")
            return redirect('accounts:index_page')
        else:
            messages.error(request, "Email or Password incorrect")
            context = {'email': email}
            return render(request, 'account/signin.html', context)

    return render(request, 'account/signin.html')


def register(request):
    forms = UserForm()
    if request.method == "POST":
        print(request.POST)
        forms = UserForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('accounts:store')
        else:

            return render(request, 'account/register.html', {'forms': forms})

    context = {'forms': forms}
    return render(request, 'account/register.html', context)


def Logout(request):
    logout(request)
    return redirect('accounts:signin')


def store(request):
    return render(request, 'store/store.html')
