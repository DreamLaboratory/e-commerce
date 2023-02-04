from django.urls import path
from .views import store_view,detail_view,search,review



urlpatterns = [
    path(
        'store-list/',store_view.store_view,name = 'store'
    ),
    path(
        "store-list/category/<slug:category_slug>/",store_view.store_view,name = 'product_list_view'
        ),
    path(
        'store-list/category/<slug:category_slug>/<slug:product_slug>/', detail_view.product_detail_view, name='product_detail_view'
    ),
    path(
        'search/', search.search, name='search'
    ),
    path(
        'review/add/<int:product_id>', review.add_review, name='add_review')

]