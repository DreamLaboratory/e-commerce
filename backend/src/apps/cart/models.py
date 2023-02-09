from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from ..common.models import BaseModel
from ..store.models.product import Product
from ..store.models.variants import ProductVariants

# Account
User = get_user_model()


class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carts")  # must be OneToOneField

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

    def __str__(self):
        return f"{self.user}"


# Product item in cart
class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="cart_items")
    variations = models.ManyToManyField(ProductVariants, blank=True)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Cart Item"
        verbose_name_plural = "Cart Items"

    def __str__(self):
        return f"{self.product}"
