from ..common.models import BaseModel
from django.db import models
from django.contrib.auth import get_user_model
from ..store.models.product import Product
from ..store.models.variant import ProductVariant
from .choose import StatusChoices

# Create your models here.

User = get_user_model()


class Cart(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="carts", null=True, blank=True)
    cart_id_pk = models.CharField(max_length=255, null=True, blank=True, unique=True)

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
    variants = models.ManyToManyField(ProductVariant)
    status = models.CharField(max_length=15, choices=StatusChoices.choices, default=StatusChoices.ACTIVE)

    class Meta:
        ordering = ["-created_date"]
        verbose_name = "Cart Item"
        verbose_name_plural = "Cart Items"

    def __str__(self):
        return str(self.product)
