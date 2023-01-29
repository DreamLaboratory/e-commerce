from django.shortcuts import render
from ..models.product import Product
from ..models.category import Category



def detail_view(request,pk):
    product = Product.objects.get(id = pk)
    return render(
        request,
        'store/product_detail.html',
        context = {
            'product':product
        }
    )


