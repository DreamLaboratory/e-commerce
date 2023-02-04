from ..models.product import Product
from django.shortcuts import render
from ..models.category import Category
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.db.models import Q 
# Create your views here.


def product_list_view(request, category_slug=None):

    price_min = request.GET.get("min")
    price_max = request.GET.get("max")
    products = Product.objects.filter(is_availabel=True)

    

    if price_max and price_min:
        print("min max")
        products = products.filter(price__gte=price_min, price__lte=price_max)

    if category_slug and (price_max == None and price_min == None):
        print("category")
        category = Category.objects.get(slug=category_slug)
        products = Product.objects.filter(category=category, is_availabel=True)

    elif category_slug and price_min and price_max:
        print("category min max ")
        category = Category.objects.get(slug=category_slug)
        products = products.filter(price__gte=price_min, price__lte=price_max)

    products_count = products.count()
    page = request.GET.get("page")
    paginator = Paginator(products, 2)
    products = paginator.get_page(page)

    context = {"products": products, "products_count": products_count}
    return render(request=request, template_name="product/store.html", context=context)


def search_view(request):
    products=Product.objects.all()
    if 'q' in request.GET:
        if request.method == "GET":
            search_product=request.GET.get('q')
            if search_product:    
                products=Product.objects.filter(Q(name__icontains=search_product) | Q(description__icontains=search_product) ,is_availabel=True)
        
    else:
        return HttpResponse('You can\'n use any letter other than q  ')
    context={
        'products':products,
    }
    return render(request=request,template_name='product/store.html',context=context)
    
def product_detail_view(request,category_slug=None,product_slug=None):

    products=Product.objects.filter()

    return render(request,template_name='product/detail.html')




    
