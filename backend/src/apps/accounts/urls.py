from django.urls import path
from .views import index, register, login,forgot_password,auth_email,redirect_login
from .activate import activate_decode

urlpatterns = [
    path("", index, name="index"),
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path("forgot_password/<uidb64>/", forgot_password, name="forgot_password"),
    path("auth_email/", auth_email, name="auth_email"),
    path("activate/<uidb64>/", activate_decode, name="activate_decode"),
    path("redirect_login/", redirect_login, name="redirect_login"),
]

