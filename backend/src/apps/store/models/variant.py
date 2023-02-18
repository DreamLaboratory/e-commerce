from ...common.models import BaseModel
from django.db import models
from .product import Product
from ...common.choices import VariantCategory

from ..manager import ProductVariantManager


class ProductVariant(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variants")
    variant_category = models.CharField(max_length=10, choices=VariantCategory.choices, default=VariantCategory.SIZE)
    variant_value = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    objects = ProductVariantManager()

    def __str__(self) -> str:
        return f"{self.variant_category} - {self.variant_value}"

    class Meta:
        verbose_name = "ProductVaraint"
        verbose_name_plural = "ProductVaraints"
