from django.urls import path
from ..store.views.product import product_list_view, search, product_detail_view

urlpatterns = [
    path("search/", search, name="search"),
    path("category/<slug:category_slug>/", product_list_view, name="product_list_view"),
    path("", product_list_view, name="product_list_view"),
    path("<slug:category_slug>/<slug:product_slug>/", product_detail_view, name="product_detail_view"),

]