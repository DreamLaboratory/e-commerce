from ..forms import ProfileForm, UserUpdateForm

from ..models import UserProfile, User
from django.contrib import messages
from django.shortcuts import redirect, render
from ...common.tg_alert import tg_alert
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

@login_required(login_url='signin/')
def profile(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)           
    user_form = UserUpdateForm(instance=user)
    profile_form = ProfileForm(instance=profile)
    context = {'user_form':user_form, 'profile_form':profile_form}

    return render(request, 'account/profile.html', context)

@login_required(login_url='signin/')
def profile_save(request):
    try:   
        user = request.user
        profile = UserProfile.objects.get(user=user)
        if request.method == 'POST':
            user_form = UserUpdateForm(request.POST, instance = user)
            profile_form = ProfileForm(request.POST, request.FILES, instance = profile)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save(commit=False)
                profile_form.user = user
                profile_form.save() 
                return redirect('order:order_list')
            return redirect('accounts:register')

    except Exception as e:
        tg_alert.custom_alert(e)
        return redirect('order:order_list')
    


@login_required(login_url='signin/')
def password_update(request):
    try:
        if request.method == 'POST':
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']
            if password == confirm_password:
                user = User.objects.get(phone_number = request.user)
                user.set_password(password)
                user.save()
                messages.success(request, "Your Password has been updated")
                return redirect('order:order_list')
            messages.warning(request, "Don't password equal confirm password") 
            return redirect('order:order_list')
        return render(request, 'account/update_password.html')
    except Exception as e:
        tg_alert.custom_alert(e)
        return redirect('order:order_list')







