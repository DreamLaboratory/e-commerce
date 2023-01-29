from django.views.generic.list import ListView
from .models.product import Product

# Create your views here.


class ProductListViews(ListView):
    model = Product
    template_name = "store.html"

    def get_queryset(self):
        return Product.objects.filter(is_availabel=True)


product_list_view = ProductListViews.as_view()
