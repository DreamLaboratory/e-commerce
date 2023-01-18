from django.shortcuts import render,redirect
from .forms import RegisterForm

# Create your views here.

def index(request):
    return render(request=request,template_name='index.html')


def store(request):
    return render(request=request,template_name='store.html')

def register(request):
    forms=RegisterForm()
    print('------------',request.method.post)
    # if request.method=='POST':
    #     forms=RegisterForm(request.method.POST)
    #     if forms.is_valid():
    #         forms.save()
    #         return redirect('/login/')
    return render(request=request,template_name='register/register.html',context={"forms":forms})
        