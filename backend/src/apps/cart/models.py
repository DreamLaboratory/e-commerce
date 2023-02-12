from ..common.models import BaseModel
from django.db import models
from django.contrib.auth import get_user_model
from ..store.models.product import Product

# Create your models here.

User = get_user_model()


class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carts")

    class Meta:
        ordering = ["-created_date"]
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

    def __str__(self):
        return str(self.user)


class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="cartitems")
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["-created_date"]
        verbose_name = "Cart Item"
        verbose_name_plural = "Cart Items"

    def __str__(self):
        return str(self.product)
