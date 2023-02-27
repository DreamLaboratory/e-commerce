from django.urls import path

from .views.views import product_list_view, search, product_detail_view, review_product

urlpatterns = [
    path('list/', product_list_view, name='product_list_view'),

    path('list/<slug:category_slug>/',
         product_list_view, name='product_list_view'),

    path('<slug:category_slug>/<slug:product_slug>/',
         product_detail_view, name='product_detail_view'),

    path('search/', search, name='search'),

    
    path('add_review/', review_product, name='review_product'),
    

]
