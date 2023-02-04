from django.urls import path
from .views.product import product_list_view, search_view, product_detail_view

urlpatterns = [
    path("list/", product_list_view, name="product_list_view"),
    path("category/<slug:category_slug>/", product_list_view, name="product_list_view"),
    path("search/", search_view, name="search_view"),
    path("product_detail/<slug:category_slug>/<slug:product_slug>", product_detail_view, name="product_detail_view"),
]
