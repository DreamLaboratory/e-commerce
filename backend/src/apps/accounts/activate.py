from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_text
from django.http import HttpResponse
from django.contrib.auth import get_user_model


def activate_decode(request, uidb64):
    try:

        User = get_user_model()
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(email=uid)
        user.is_active = True
        user.save()
        return HttpResponse(uid)
    except Exception as ex:
        return ex
