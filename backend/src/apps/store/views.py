from .models.product import Product
from django.views.generic.list import ListView

# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = "store.html"
    context_object_name = "products"
    paginate_by = 10

    def get_queryset(self):
        return Product.objects.filter(is_available=True)


product_list_view = ProductListView.as_view()
