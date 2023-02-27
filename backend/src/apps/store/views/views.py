from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages

from ..models.product import Product, Product_Image
from ..models.category import Category
from django.core.paginator import Paginator
from ..models.review import Review
from ..models.variants import ProductVariants
from ...common.cart_item_id import _cart_id
from ..form_review import ReviewForm
from ...common.tg_alert import tg_alert
# Create your views here.


def product_list_view(request, category_slug=None):
    min_price = request.GET.get('min')
    max_price = request.GET.get('max')
    category = None

    products = Product.objects.filter(is_available=True)

    if min_price and max_price:
        products = products.filter(
            price__lte=max_price, price__gte=min_price)

    if category_slug:
        category = Category.objects.get(slug=category_slug)
        products = products.filter(category=category, is_available=True)

    product_count = products.count()

    page = request.GET.get('page')
    paginator = Paginator(products, 2)
    products = paginator.get_page(page)

    context = {
        'products': products,
        'product_count': product_count
    }
    return render(request, 'store/store.html', context)


def product_detail_view(request, category_slug, product_slug):
    product = Product.objects.get(
        category__slug=category_slug, slug=product_slug)
    product_images = Product_Image.objects.filter(product=product)
    product_review = Review.objects.filter(product=product)
    context = {'product': product, 'product_reviews': product_review,
               'product_images': product_images}
    return render(request, 'store/product.html', context)


def search(request):
    products = Product.objects.filter(is_available=True)
    if 'q' in request.GET:
        if q := request.GET['q']:
            products = products.filter(
                Q(name__icontains=q) | Q(description__icontains=q))
            product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)

def review_product(request):
    try:
        url = request.META.get("HTTP_REFERER")
        if request.method == 'POST':
            data = Review()
            data.user = request.user
            data.product_id = request.POST['product_id']
            data.rate = request.POST['rating']
            data.description = request.POST['description']
            data.save()
            messages.success(request, 'Success add review')
            return redirect(url)
    except Exception as e:
        messages.error(request, 'Xatolik')
        tg_alert.custom_alert(e)
        return redirect(url)


