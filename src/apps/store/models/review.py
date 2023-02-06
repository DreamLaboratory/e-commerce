from django.db import models
from ...common.models import BaseModel
from ...accounts.models import Account
from .product import Product
from django.core.exceptions import ValidationError


def validate_desc(value):
    # TODO move to forms.py
    # list of bad words
    bad_words = ["yomon"]
    # check if bad words in review description
    if any(word in value for word in bad_words):
        raise ValidationError("Bad words in review description")


class Review(BaseModel):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    desc = models.TextField()
    status = models.BooleanField(default=False)
    ip = models.GenericIPAddressField(blank=True, null=True)
    rating = models.IntegerField(default=0)
    # reply = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ["-created_at"]
