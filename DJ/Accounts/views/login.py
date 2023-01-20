from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        email = request.POST.get('email',None)
        password = request.POST.get('password',None)
        user = authenticate(
            request,
            email = email,
            password = password
        )
        if user:
            login(request,user)
            return redirect('index')
        else:
            return redirect('login')

    return render(
        request=request,
        template_name='accounts/login.html',
    )