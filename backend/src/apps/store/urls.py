from django.urls import path

from .views import product_list,product_list_view, search, product_detail_view

urlpatterns = [
    path("list/", product_list, name="product_list_view"),
    path("list/", product_list_view, name="product_list_view"),
    path("list/<slug:category_slug>/", product_list_view, name="product_list_view"),
    path("search/", search, name="search"),
    path("<slug:category_slug>/<slug:product_slug>/", product_detail_view, name="product_detail_view"),
]
