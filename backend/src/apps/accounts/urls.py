from django.urls import path
from .views import store,index

urlpatterns = [
   path('',index,name='index'),
   path('store/',store,name='store'),


]