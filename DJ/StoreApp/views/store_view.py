from django.shortcuts import render
from ..models.product import Product
from ..models.category import Category
from django.core.paginator import Paginator


def store_view(request, category_slug=None):
    category = None
    products = Product.objects.filter(is_available=True)
    min_price = request.GET.get('min', None)
    max_price = request.GET.get('max', None)

    if min_price and max_price and category_slug:
        category = Category.objects.get(slug=category_slug)
        products = Product.objects.filter(price__gte=min_price, price__lte=max_price, category=category)

    elif min_price and max_price:
        products = Product.objects.filter(price__gte=min_price, price__lte=max_price)


    elif category_slug is not None:
        category = Category.objects.get(slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True)

    count_products = products.count()
    page = request.GET.get('page')
    paginator = Paginator(products, 2)
    products = paginator.get_page(page)

    return render(
        request,
        'store/store.html',
        {'products': products,
         'count_products': count_products}
    )
