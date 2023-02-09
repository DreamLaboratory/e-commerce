from django.shortcuts import render,redirect

def success_view(request):
    return render(
        request,
        'parts/success.html'
    )