from django.db import models
from ...common.models import BaseModel
from ...accounts.models import Account
from .product import Product
from django.core.exceptions import ValidationError


BAD_WORDS = ["yomon", "waterfall", "enterprise"]


def validate_no_bad_words(desc):
    if any([word in desc.lower() for word in BAD_WORDS]):
        raise ValidationError("This review contains bad words!")


class Review(BaseModel):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    desc = models.TextField(validators=[validate_no_bad_words])
    status = models.BooleanField(default=False)
    ip = models.GenericIPAddressField(blank=True, null=True)
    rating = models.FloatField(default=0)
    # reply = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ["-created_at"]
