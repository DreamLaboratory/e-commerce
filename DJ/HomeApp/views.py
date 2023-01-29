from django.shortcuts import render
import sys
sys.path.append("..")

from django.shortcuts import render
from StoreApp.models.product import Product




def index_view(request):
    objects = Product.objects.all()
    return render(
        request,
        'index.html',
        {'products':objects}
    )

