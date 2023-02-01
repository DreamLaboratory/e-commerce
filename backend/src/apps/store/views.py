from django.views.generic.list import ListView
from .models.product import Product
from django.shortcuts import render
from .models.category import Category
from django.core.paginator import Paginator
# Create your views here.

def product_list_view(request,category_slug=None):


    price_min=request.GET.get('min')
    price_max=request.GET.get('max')
    products=Product.objects.filter(is_availabel=True)

    if price_max and price_min:
        print('min max')
        products=products.filter(price__gte=price_min, price__lte=price_max)

    if category_slug and (price_max == None and price_min ==None ):
        print('category')
        category=Category.objects.get(slug=category_slug)
        products=Product.objects.filter(category=category,is_availabel=True)
    
    elif category_slug and price_min and price_max:
        print('category min max ')
        category=Category.objects.get(slug=category_slug)
        products=products.filter(price__gte=price_min, price__lte=price_max)

    products_count=products.count()
    page=request.GET.get('page')
    paginator=Paginator(products,2)
    products=paginator.get_page(page)

    context={
        'products':products,
        'products_count':products_count
    }
    return render(request=request,template_name='product/store.html',context=context)

def detail(request):
    pass