from django.shortcuts import render
from .models.product import Product
from django.views.generic.list import ListView


class ProductListView(ListView):
    model = Product
    template_name = "store.html"
    context_object_name = "products"
    paginate_by = 10

    def get_queryset(self):
        return Product.objects.filter(is_available=True)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['prod_count'] = Product.objects.filter(is_available=True).count
        return context

product_list_view = ProductListView.as_view()
