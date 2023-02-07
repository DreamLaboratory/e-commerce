from django.db import models
import sys
from .product import Product

from HomeApp.models import BaseModel
from HomeApp.file_renamer import PathAndRename

sys.path.append("...")
path_and_rename = PathAndRename('products')


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to=path_and_rename)

    @property
    def get_image_url(self):
        return self.image.url if self.image and hasattr(self.image, 'url') else ""

    class Meta:
        verbose_name = 'Product image'
        verbose_name_plural = "Product images"
        ordering = ['-created_at']

    def __str__(self):
        return str(self.product)
