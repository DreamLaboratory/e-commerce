from django.urls import path
from .views import login,logout,register,success,token_send_mail,reset_password,profile_edit


urlpatterns = [
    path(
          "login/",login.login_view,name='login'
    ),
    path(
          "register/",register.register_view,name = 'register'
    ),
    path(
         "logout/",logout.logut_view,name = 'logout',
    ),
    path(
         "token/",token_send_mail.token_view,name= 'token'
    ),
    path(
         "success/",success.success_view,name = 'success',
    ),
    path(
        "verify/<auth_token>/", token_send_mail.verify , name='verify',
    ),
    path(
        "error/",token_send_mail.error_page, name='error',
    ),
    path(
        "reset-password/",reset_password.forget_password , name='reset-password',
    ),
    path(
        "reset_password/<uidb64>/", reset_password.reset_password, name='reset_password',
    ),
    path(
        "profile-edit/", profile_edit.profile_edit, name='profile_edit',
    ),
    path(
        "profile-save/", profile_edit.profile_save, name='profile_save',
    ),
    path(
        "user-password-change/", profile_edit.password_change, name='password_change',
    ),
]

