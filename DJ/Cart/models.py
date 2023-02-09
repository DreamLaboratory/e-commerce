from django.db import models
import sys
sys.path.append("...")
from HomeApp.models import BaseModel
from django.contrib.auth import get_user_model
from StoreApp.models.product import Product
from StoreApp.models.variants import ProductVariants

User = get_user_model()


class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user}'


class CartItems(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.PositiveIntegerField(default=1)
    variants = models.ManyToManyField(ProductVariants, blank=True)

    class Meta:
        verbose_name = 'Cart Item'
        verbose_name_plural = "Cart Items"
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.product}'
