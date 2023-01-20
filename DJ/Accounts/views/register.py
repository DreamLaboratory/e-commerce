from django.contrib import messages
from django.shortcuts import render,redirect
from ..forms import RegistrationForm
from ..models import Account




def register_view(request):
    form = RegistrationForm()
    if request.method=='POST':
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_form = form.save(commit=False)
            password = form.cleaned_data.get('password')
            new_form.set_password(password)
            new_form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Account Created for {username}")
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(
        request,
        'accounts/register.html',
        context={'form':form}
    )

# if request.method == "POST":
#     first_name = request.POST.get('first_name',None)
#     last_name = request.POST.get('last_name',None)
#     email = request.POST.get('email','None')
#     phone_number = request.POST.get('phone',None)
#     password1 = request.POST.get('password1')
#     password2 = request.POST.get('password2')
#     username = request.POST.get('username')
#
#
#
#     if password1==password2:
#         user=Account.objects.create(
#             first_name=first_name,
#             last_name=last_name,
#             username=username,
#             email =email,
#             password=password1,
#             phone_number=phone_number,
#         )
#
#         user.set_password(password1)
#         user.save()
#         if user:
#             return redirect('login')