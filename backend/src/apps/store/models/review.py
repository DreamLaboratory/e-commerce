from ...common.models import BaseModel
from django.db import models
from ...accounts.models import MyUser
from .product import Product
from django.core.exceptions import ValidationError

  


class Reviews(BaseModel):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    ip = models.GenericIPAddressField(null=True, blank=True)
    desc = models.TextField()
    status = models.BooleanField(default=False)
    rating = models.FloatField() 
    # reply = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ["-created_date"]


# TODO: centray: xato chiqsa emailga borib turish
