from django.urls import path

from .views import activate, index, login, logout_user, register, reset_password

urlpatterns = [
    path("", index.index_page, name="index_page"),
    path("register/", register.register, name="register"),
    path("login/", login.login, name="login"),
    path("logout/", logout_user.logout_user, name="logout_user"),
    path("activate/<uidb64>/", activate.activate, name="activate"),
    # reset password
    path("forgot-password/", reset_password.forgot_password, name="forgot_password"),
    path("verify-password/<uidb64>/", reset_password.validate_password, name="validate_password"),
]
