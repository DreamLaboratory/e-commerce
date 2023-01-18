from django.urls import path
from .views import store,index,register

urlpatterns = [
   path('',index,name='index'),
   path('store/',store,name='store'),
   path('register/',register,name='register'),
]

