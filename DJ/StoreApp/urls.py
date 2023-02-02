from django.urls import path
from .views import store_view,detail_view,search



urlpatterns = [
    path(
        'store-list/',store_view.store_view,name = 'store'
    ),
    path(
        "store-list/<slug:category_slug>/",store_view.store_view,name = 'product_list_view'
        ),
    path(
        'store-list/<slug:category_slug>/<slug:product_slug>/', detail_view.product_detail_view, name='product_detail_view'
    ),
    path(
        'search/', search.search, name='search'
    ),
]