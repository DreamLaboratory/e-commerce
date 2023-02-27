from django.urls import path
from .views.product import product_list_view, search_view, product_detail_view
from .views.review import add_review


urlpatterns = [
    path("", product_list_view, name="product_list_view"),
    path("review/add/<int:product_id>/", add_review, name="add_review"),
    path("category/<slug:category_slug>/", product_list_view, name="product_list_view"),
    path("search/", search_view, name="search_view"),
    path("product_detail/<slug:category_slug>/<slug:product_slug>/", product_detail_view, name="product_detail_view"),
]
