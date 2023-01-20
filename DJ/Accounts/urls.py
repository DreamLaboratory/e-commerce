from django.urls import path
from .views import login,logout,register


urlpatterns = [
    path(
          "login/",login.login_view,name='login'
    ),
    path(
          "register/",register.register_view,name = 'register'
    ),
    path(
        "logout/",logout.logut_view,name = 'logout',
    )

]