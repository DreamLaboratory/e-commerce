import logging

from django.shortcuts import render, redirect
from ..models import Profile, Account
from ..form.profile_form import ProfileForm,UserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def profile_edit(request):
    form = ProfileForm()
    return render(
        request,
        'accounts/profile_edit.html',
        context={'form': form}
    )


@login_required(login_url="/login/")
def profile_save(request):
    try:
            user = request.user
            profile = Profile.objects.get(user=user)
            if request.method == 'POST':
                user_form = UserForm(request.POST,instance=user)
                profile_form = ProfileForm(request.POST,request.FILES,instance=profile)

                if user_form.is_valid() and profile_form.is_valid():
                    user_form.save()
                    profile_form.save()
                    messages.success(request, 'Profile Edit Success')
                    return redirect('order_list')
            else:
                user_form = UserForm(instance=Account)
                profile_form = ProfileForm(instance=profile)
            context = {
                'user_form': user_form,
                'profile_form': profile_form,
            }
            return render(
                request,
                'accounts/profile_edit.html',
                context
            )
    except Exception as e:
        logging.error(e)
        return redirect('order_list')


def password_change(request):
    if request.method == "POST":
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            print(password2,password1)
            if password2==password1:
                account = Account.objects.get(email=request.user.email)
                account.set_password(password1)
                account.save()
                messages.success(request,'Your Password success Change')
    return render(
        request,
        'accounts/change_password.html',
    )