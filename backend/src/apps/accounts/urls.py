from django.urls import path
from .views import store,index,register,login

urlpatterns = [
   path('',index,name='index'),
   path('store/',store,name='store'),
   path('login/',login,name='login'),
   path('register/',register,name='register'),
]

