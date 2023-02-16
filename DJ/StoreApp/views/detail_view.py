from django.shortcuts import render
from ..models.product import Product
from ..models.category import Category
from ..models.variants import ProductVariants

def product_detail_view(request, category_slug=None, product_slug=None):
    product = Product.objects.get(
        category__slug=category_slug, slug=product_slug
    )

    product_reviews = product.reviews.filter(product=product, status=True)
    image_product = product.images.filter(product=product)
    average_rating = str(product.average_rating)
    # variants_color = product.variants.colors()
    # variant_size = product.variants.size()
    # product_size = ProductVariants.objects.size().filter(product=product)
    product_color = ProductVariants.objects.colors().filter(product=product)
    context = {
        'product_reviews': product_reviews,
        "image_product": image_product,
        'product': product,
        'average_rating': average_rating,
        "product_color":product_color,

    }
    return render(
        request,
        'store/product_detail.html',
        context
    )
