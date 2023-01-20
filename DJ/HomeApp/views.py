from django.shortcuts import render


def IndexView(request):
    return render(
        request=request,
        template_name='index.html'
    )
