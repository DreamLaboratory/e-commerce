from django.urls import path
from .views import store_view,detail_view



urlpatterns = [
    path(
        'store/',store_view.store_view,name = 'store'
    ),
    path(
        'detail/<int:pk>/', detail_view.detail_view, name='detail'
    ),
]