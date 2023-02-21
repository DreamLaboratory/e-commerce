from django.db import models
from .product import Product
import sys
from ..managers import ProductVariantsManager
sys.path.append("...")
from HomeApp.models import BaseModel


class CategoryVariants(models.TextChoices):
    SIZE = "size"
    COLOR = 'color'


class ProductVariants(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    variant_category = models.CharField(max_length=255, choices=CategoryVariants.choices, default=CategoryVariants.SIZE)
    variant_value = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    objects = ProductVariantsManager()

    class Meta:
        verbose_name = 'Product Variant'
        verbose_name_plural = "Products Variants"

    def __str__(self):
        return f"{self.variant_category}-{self.variant_value}"
