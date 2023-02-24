from django.shortcuts import render


def order_view(request):
    return render(request=request, template_name="product/order.html")
