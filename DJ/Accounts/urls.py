from django.urls import path
from .views import login,logout,register,success,token_send_mail


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
]