from django.shortcuts import render
from ..models.product import Product
from django.db.models import Q


def search(request):
	products = Product.objects.filter(is_available = True)
	if 'q' in request.GET:
		if q:=request.GET.get('q'):
			products = products.filter(
				Q(name__icontains=q) | Q(descriptions__icontains=q)
			)
			# products = products.filter(name__icontains=q)
			product_count = products.count()

		context = {
		"products":products,
		"count_products":product_count
		}

	return render(

		request,
		  'store/store.html',
		  context
		  )

