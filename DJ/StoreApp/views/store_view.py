from django.shortcuts import render
from ..models.product import Product
from ..models.category import Category


def store_view(request):
    objects = Product.objects.all()
    return render(
        request,
        'store/store.html',
        {'products':objects}
    )
