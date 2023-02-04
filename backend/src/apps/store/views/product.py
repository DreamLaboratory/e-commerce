import logging

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

from ..models.category import Category
from ..models.product import Product, ProductImage
from ..models.review import Review

# import logging


logger = logging.getLogger(__name__)


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

        return render(request, "store/store.html", {"products": products, "product_count": product_count})
    except Exception as e:
        logger.error(e)
        return render(request, "store/store.html", {"products": None, "product_count": 0})


# url/<slug:category_slug>/<slug:product_slug>/
def product_detail_view(request, category_slug, product_slug):
    product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    product_reviews = Review.objects.filter(product=product)
    product_images = ProductImage.objects.filter(product=product)
    context = {
        "product": product,
        "product_reviews": product_reviews,
        "product_images": product_images,
    }
    return render(request, "store/product_detail.html", context)


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
    print(context)
    return render(request, "store/store.html", context)
