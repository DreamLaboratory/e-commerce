from django.db import models
import sys


sys.path.append("...")
from HomeApp.models import BaseModel
from django.contrib.auth import get_user_model
from StoreApp.models.product import Product
from StoreApp.models.variants import ProductVariants

User = get_user_model()


class Cart(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='carts',null=True,blank=True)
    cart_id = models.CharField(max_length=200,null=True,blank=True)

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user}'


class StatusChoices(models.TextChoices):
    ACTIVE = 'active'
    INACTIVE = 'inactive'


class CartItems(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.PositiveIntegerField(default=1)
    variants = models.ManyToManyField(ProductVariants, blank=True)
    status = models.CharField(max_length=100, choices=StatusChoices.choices, default=StatusChoices.ACTIVE)

    class Meta:
        verbose_name = 'Cart Item'
        verbose_name_plural = "Cart Items"
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.cart}'
