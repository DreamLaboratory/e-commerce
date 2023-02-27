from django.contrib.auth import get_user_model
from django.db import models

from ..common.cartstatus import CartStatus
from ..common.models import BaseModel
from ..store.models.product import Product
from ..store.models.variants import ProductVariants

User = get_user_model()

class Cart(BaseModel):
    user = models.OneToOneField(User ,on_delete=models.CASCADE, related_name='cart', blank=True, null=True)
    cart_id_pk = models.CharField(max_length=255, blank=True, null=True, unique=True)

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'
    
    def __str__(self):
        return str(self.user)


class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    variation = models.ManyToManyField(ProductVariants, blank=True)
    status = models.CharField(max_length=20, choices=CartStatus.choices, default=CartStatus.ACTIVE)

    class Meta:
        ordering = ['-date_joined']
        verbose_name  = 'Cart Item'
        verbose_name_plural = 'Cart Items'

    def __str__(self) -> str:
        return f"{self.cart} - {self.product}"