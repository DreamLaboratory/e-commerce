from django.urls import path

from .views.index import index_page
from .views.register import register
from .views.sign_in import sign_in
from .views.log_out import log_out
from .views.activate import activate
from .views.reset_password import forgot_password, validate_password


urlpatterns = [
    path("", index_page, name="index_page"),
    path("register/", register, name="register"),
    path("sign-in/", sign_in, name="sign_in"),
    path("log_out/", log_out, name="log_out"),
    path("activate/<str:uidb64>/", activate, name="activate"),
    # reset password
    path("forgot-password/", forgot_password, name="forgot_password"),
    path("verify-password/<uidb64>/", validate_password, name="validate_password"),
]
