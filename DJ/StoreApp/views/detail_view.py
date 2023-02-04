from django.shortcuts import render
from ..models.product import Product
from ..models.category import Category
from ..models.review import Review
from ..models.image_product import ProductImage


def product_detail_view(request,category_slug=None,product_slug = None):
    product = Product.objects.get(
        category__slug = category_slug,slug = product_slug
    )
    product_reviews = Review.objects.filter(product = product)
    image_product = ProductImage.objects.filter(product = product)

    context = {
        'product_reviews':product_reviews,
        "image_product":image_product,
        'product':product
        }
    return render(
        request,
        'store/product_detail.html',
        context
    )


