from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib import auth
from django.http import HttpResponse
# from .models import MyUser
# Create your views here.

def index(request):
    return render(request=request,template_name='index.html')


def store(request):
    return render(request=request,template_name='store.html')

def register(request):
    forms=RegisterForm()
    if request.method=='POST':
        forms=RegisterForm(request.POST)
        if forms.is_valid():
            new_forms=forms.save(commit=False)
            password=forms.cleaned_data.get('password')
            new_forms.set_password(password)
            new_forms.save()
            username=forms.cleaned_data.get('username')
            messages.success(request,f'User created for {username}')
            return redirect('accounts:login')
    return render(request=request,template_name='register/register.html',context={"forms":forms})

def login(request):

    if request.user.is_authenticated:
        return redirect('accounts:index')

    if request.method=="POST":

        email=request.POST.get('email')
        password=request.POST.get('password')
        user=auth.authenticate(request,email=email,password=password)

        if user:
            auth.login(request,user)
            messages.success(request,'You are soccessed login')
            return redirect('accounts:index')
        else:
            return HttpResponse('Login Failed')
    

    return render(request,'register/login.html')