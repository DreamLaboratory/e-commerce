from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from ..models import Account, Profile
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number', None)
        password = request.POST.get('password', None)
        user = authenticate(
            request,
            phone_number=phone_number,
            password=password
        )

        if user is None:
            messages.success(request, "User Not Found !")
            return redirect('login')

        profile_obj = Profile.objects.get(phone_number=phone_number)

        if not profile_obj.is_verified:
            messages.success(request, "Profile is not verified check your phone number!")
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
