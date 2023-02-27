from django.urls import path

from .views.Login import Login
from .views.register import register
from .views.index import index_page
from .views.logout import Logout
from .views.activate import activate
from .views.forgotpassword import forgotpassword, resetpass
from .views.profile_update import profile_save, profile, password_update


urlpatterns = [

    path("", index_page, name="index_page"),
    path("register/", register, name='register'),
    path("signin/", Login, name='signin'),
    path('logout/', Logout, name="logout"),

    #verify
    path("activate/<uidb64>/", activate, name='activate'),
    path('verifyemail/', forgotpassword, name='verifyemail'),
    path('resetpassword/<uidb64>/', resetpass, name='resetpassword'),

    #update
    path('update/profile', profile, name='profile_update'),
    path('update/', profile_save, name='profile_save'),
    path('update/password', password_update, name='update_password'),

]

