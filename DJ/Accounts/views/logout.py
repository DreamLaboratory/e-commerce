from django.shortcuts import render,redirect
from django.contrib.auth import logout




def logut_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')

    return render(
        request,
        'account/logout.html'
    )
