from django.shortcuts import render,redirect
from .forms import RegisterForm

# Create your views here.

def index(request):
    return render(request=request,template_name='index.html')


def store(request):
    return render(request=request,template_name='store.html')

def register(request):
    # data=request.POST['first_name']
    
    forms=RegisterForm(request.method)

    if request.method=='POST':
        pass
    return render(request=request,template_name='register/register.html',context={"forms":forms})
        
   
        