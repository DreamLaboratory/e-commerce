from django.views.generic.base import TemplateView
from ...store.models.product import Product


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex["products"] = Product.objects.all()
        return contex


index_page = IndexView.as_view()
