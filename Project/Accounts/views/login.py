from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from ..models import Account, Profile
from django.contrib import messages





def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        user = authenticate(
            request,
            email=email,
            password=password
        )
        if user is None:
            messages.success(request, "User Not Found !")
            return redirect('login')

        profile_obj = Profile.objects.get(email=email)

        if not profile_obj.is_verified:
            messages.success(request, "Profile is not verified check your email!")
            return redirect('login')

        if user:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')

    return render(
        request=request,
        template_name='accounts/login.html',
    )
