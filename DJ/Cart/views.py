from django.shortcuts import render,redirect
from django.db.models import Sum,F
from django.db import models
from StoreApp.models.product import Product
from StoreApp.models.variants import ProductVariants
from .models import Cart,CartItems,StatusChoices
from decimal import Decimal
def add_cart(request):
    if request.method != 'POST':
        return render(request, 'store/cart_items.html', {"cart_items": None})

    product_id = request.POST.get('product_id',None)
    color = request.POST.get('color',None)
    size = request.POST.get('size',None)
    variations = ProductVariants.objects.filter(product_id=product_id, variant_value__in=[size, color])
    cart,created = Cart.objects.get_or_create(user = request.user)
    cart_item,created = CartItems.objects.get_or_create(cart=cart,product_id=product_id)
    print(variations)

    for variation in variations:
        cart_item.variants.add(variation)

    cart_item.save()
    return redirect('carts')


def carts(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItems.objects.filter(cart=cart, status=StatusChoices.ACTIVE)
    total_price = cart_items.aggregate(
        total_price=Sum(
            F("product__price") * F("quantity"), output_field=models.DecimalField(max_digits=10, decimal_places=2)
        )
    )["total_price"]

    delevery = Decimal(total_price * Decimal(0.1)).quantize(Decimal("0.01"))  # 10% of total price
    grand_total = total_price + delevery

    context = {"cart_items": cart_items, "total_price": total_price, "delevery": delevery, "grand_total": grand_total}
    return render(request, "store/cart_items.html", context)


