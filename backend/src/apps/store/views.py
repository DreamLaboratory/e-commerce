from .models.category import Category
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

    def get_context_data(self, **kwargs):
        data = super(ProductListView, self).get_context_data(**kwargs)
        categories = Category.objects.all()
        data["categories"] = categories
        print(1111111111, data)
        return data


product_list_view = ProductListView.as_view()
