from ...common.models import BaseModel
from django.db import models
from ...accounts.models import User
from .product import Product


class Review(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, blank=True, related_name='reviews')
    status = models.BooleanField(default=True)
    rate = models.FloatField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = "Reviews"
        ordering = ['-date_joined']

    def __str__(self):
        return str(self.user)
