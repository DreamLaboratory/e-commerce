from ..forms import ProfileForm, UserUpdateForm
from django.contrib import messages
from django.shortcuts import redirect, render
def profile(request):

    if request.POST:
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user)
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if profile_form.is_valid and user_form.is_valid:
            profile_form.save()
            user_form.save()
            messages.success(request, "Your account updated")
            return redirect('order:order_list')
    else:
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user)
        user_form = UserUpdateForm(request.POST, instance=request.user)
    context = {'profile_form': profile_form, 'user_form':user_form}

    return render(request, 'account/profile.html', context)
            