from ...common.models import BaseModel
from django.db import models
from .product import Product
from ..managers import ProductVariansManager

class VariantChoises(models.TextChoices):
    COLOR = 'color'
    SIZE = 'size'


class ProductVariants(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    product_variant = models.CharField(max_length=255, choices=VariantChoises.choices, default=VariantChoises.COLOR)
    value = models.CharField(max_length=255)
    is_active = models.BooleanField(default=1)

    objects = ProductVariansManager()


    class Meta:
        verbose_name = 'Product Variant'
        verbose_name_plural = 'Product Variants'

    def __str__(self):
        return f"{ self.product } - { self.value }"


