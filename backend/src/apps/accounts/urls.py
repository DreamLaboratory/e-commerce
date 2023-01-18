from django.urls import path

from .views import index_page, cart_page, dashboard_page, order_complete_page, place_order_page, product_detail_page, register_page, search_result_page, signin_page, store_page

urlpatterns = [
    path("", index_page, name="index_page"),
    path("cart/", cart_page, name="cart_page"),
    path("dashboard/", dashboard_page, name="dashboard_page"),
    path("order-complete/", order_complete_page, name="order_complete_page"),
    path("place-order/", place_order_page, name="place_order_page"),
    path("product-detail/", product_detail_page, name="product_detail_page"),
    path("register/", register_page, name="register_page"),
    path("search-result/", search_result_page, name="search_result_page"),
    path("sign-in/", signin_page, name="signin_page"),
    path("store/", store_page, name="store_page"),
]
