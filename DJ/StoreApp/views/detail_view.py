from django.shortcuts import render
from ..models.product import Product
from ..models.category import Category



def product_detail_view(request,category_slug=None,product_slug = None):
    product = Product.objects.get(
        category__slug = category_slug,slug = product_slug
    )
    return render(
        request,
        'store/product_detail.html',
        context = {
            'product':product
        }
    )


