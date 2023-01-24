from django.http import HttpResponse
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model

def activate(request, uidb64):
    try:
        User = get_user_model()
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(email=uid)
        user.is_active = True
        user.save()
        print(uid)
        return HttpResponse(uid)
    except Exception as e:
        return HttpResponse("Invalid activation link!")