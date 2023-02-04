from django.shortcuts import render

from ..models.category import Category
from ..models.product import Product
from ..models.review import Review
from django.views.generic.list import ListView
from django.core.paginator import Paginator
from django.db.models import Q


# class ProductListView(ListView):
#     model = Product
#     template_name = "store.html"
#     context_object_name = "products"
#     paginate_by = 10
#
#     def get_queryset(self):
#         return Product.objects.filter(is_available=True)
#
#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         context['prod_count'] = Product.objects.filter(is_available=True).count()
#         return context
#
#
# product_list_view = ProductListView.as_view()


def product_list_view(request, category_slug=None):
    try:
        min_price = request.GET.get('min')
        max_price = request.GET.get('max')
        products = Product.objects.filter(is_available=True)
        if min_price and max_price:
            products = products.filter(price__gte=min_price, price__lte=max_price)
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            products = products.filter(is_available=True, category=category)

        prod_count = products.filter(is_available=True).count()
        page = request.GET.get("page")
        paginator = Paginator(products, 10)
        products = paginator.get_page(page)

        return render(request, "store/store.html", {"products": products, 'prod_count': prod_count})
    except Exception as e:
        print(e)
        return render(request, "store/store.html", {"products": None, 'prod_count': 0})


def product_detail_view(request, category_slug, product_slug):
    product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    product_review = Review.objects.filter(product=product)
    context = {
        'product': product,
        'product_reviews': product_review,
    }
    return render(request, 'store/product-detail.html', context)


def search(request):
    products = Product.objects.filter(is_available=True)
    if "q" in request.GET:
        if q := request.GET["q"]:
            products = products.filter(Q(name__icontains=q) | Q(description__icontains=q))
            product_count = products.count()

    context = {
        "products": products,
        "product_count": product_count
    }

    return render(request, "store/store.html", context)
