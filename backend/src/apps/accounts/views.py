from django.views.generic.base import TemplateView


# Create your views here.


class IndexView(TemplateView):
    template_name = "index.html"


index_page = IndexView.as_view()


class CartView(TemplateView):
    template_name = "cart.html"


cart_page = CartView.as_view()


class DashboardView(TemplateView):
    template_name = "dashboard.html"


dashboard_page = DashboardView.as_view()


class OrderCompleteView(TemplateView):
    template_name = "order_complete.html"


order_complete_page = OrderCompleteView.as_view()


class PlaceOrderView(TemplateView):
    template_name = "place-order.html"


place_order_page = PlaceOrderView.as_view()


class ProductDetailView(TemplateView):
    template_name = "product-detail.html"


product_detail_page = ProductDetailView.as_view()


class RegisterView(TemplateView):
    template_name = "register.html"


register_page = RegisterView.as_view()


class SearchResultView(TemplateView):
    template_name = "search-result.html"


search_result_page = SearchResultView.as_view()


class SignInView(TemplateView):
    template_name = "signin.html"


signin_page = SignInView.as_view()


class StoreView(TemplateView):
    template_name = "store.html"


store_page = StoreView.as_view()
