from django.urls import path

from .views import index_page, Login, register, Logout, store

urlpatterns = [
    path("index/", index_page, name="index_page"),
    path("register/", register, name='register'),
    path("signin/", Login, name='signin'),
    path('logout/', Logout, name="logout"),


    path('store/', store, name='store'),
]
