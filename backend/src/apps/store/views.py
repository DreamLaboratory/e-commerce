from .models.product import Product
from django.shortcuts import render
from .models.category import Category
from django.core.paginator import Paginator

# import logging

import logging

logger = logging.getLogger(__name__)

from django.db.models import Q

# class ProductListView(ListView):
#     model = Product
#     template_name = "store.html"
#     context_object_name = "products"
#     paginate_by = 10

#     def get_queryset(self):
#         return Product.objects.filter(is_available=True)


# product_list_view = ProductListView.as_view()


# url/store/list/<slug:category_slug>/?min=100&max=200


def product_list_view(request, category_slug=None):
    # TODO try except
    try:
        min_price = request.GET.get("min")
        max_price = request.GET.get("max")

        products = Product.objects.filter(is_available=True)
        if min_price and max_price:
            # __gte = greater than or equal to >= and __lte = less than or equal to <=
            products = products.filter(price__gte=min_price, price__lte=max_price)
        if category_slug:  # TODO - add category filter
            category = Category.objects.get(slug=category_slug)
            products = products.filter(category=category, is_available=True)

        product_count = products.count()
        page = request.GET.get("page")
        paginator = Paginator(products, 1)
        products = paginator.get_page(page)

        return render(request, "store.html", {"products": products, "product_count": product_count})
    except Exception as e:
        logger.error(e)
        return render(request, "store.html", {"products": None, "product_count": 0})


# url/<slug:category_slug>/<slug:product_slug>/
def product_detail_view(request, category_slug, product_slug):
    product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    return render(request, "product.html", {"product": product})


def search(request):
    products = Product.objects.filter(is_available=True)
    if "q" in request.GET:
        if q := request.GET["q"]:
            products = products.filter(Q(name__icontains=q) | Q(description__icontains=q))
            product_count = products.count()

    context = {
        "products": products,
        "product_count": product_count,
    }
    return render(request, "store.html", context)
