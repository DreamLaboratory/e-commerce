from django.urls import path
from .views import product_list_view,search_view

urlpatterns = [
    path("list/", product_list_view, name="product_list_view"),
    path("category/<slug:category_slug>/", product_list_view, name="product_list_view"),
    path('search/<slug:category_slug>/',search_view,name='search_view'),
]
