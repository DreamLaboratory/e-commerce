from django.urls import path
from .views import index, register, login
from .activate import activate_decode

urlpatterns = [
    path("", index, name="index"),
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path("activate/<uidb64>/", activate_decode, name="activate_decode"),
]
