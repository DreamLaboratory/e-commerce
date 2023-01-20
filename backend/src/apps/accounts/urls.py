from django.urls import path

from .views.index import index_page
from .views.register import register
from .views.login import login
from .views.activate import activate

urlpatterns = [
    path("", index_page, name="index_page"),
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    path("activate/<uidb64>/", activate, name="activate"),
]
