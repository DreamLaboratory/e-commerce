import sys
import sys
sys.path.append("...")
from django.db import models
from HomeApp.models import BaseModel
from Accounts.models import Account
from django.contrib.auth import get_user_model
from .product import Product



class Review(BaseModel):
    user = models.ForeignKey(Account,on_delete = models.CASCADE)
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    desc = models.TextField()
    status = models.BooleanField(default = False)
    ip = models.GenericIPAddressField(null=True,blank=True)
    rating = models.IntegerField(default = 0)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ['-created_at']
