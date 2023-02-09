from django.db import models
from .product import Product
from ...common.models import BaseModel


class ImageProduct(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="detail_image_category")

    def __str__(self):
        return str(self.product)

    @property
    def get_image_url(self):
        return self.image.url if self.image and hasattr(self.image, "url") else "rasim yuq"
