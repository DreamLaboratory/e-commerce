from django.db import models
import sys
from .product import Product

from HomeApp.models import BaseModel
from HomeApp.file_renamer import PathAndRename
sys.path.append("...")
path_and_rename = PathAndRename('products')



class ProductImage(BaseModel):
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    image = models.ImageField(upload_to = path_and_rename)

    class Meta:
        verbose_name = 'Product image'
        verbose_name_plural = "Product images"
        ordering = ['-created_at']

    def __str__(self):
        return str(self.product)

