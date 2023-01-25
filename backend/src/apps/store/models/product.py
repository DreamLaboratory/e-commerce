from django.utils.text import slugify
from django.db import models
from django.utils.translation import gettext_lazy as _

from ...common.renamed import PathAndRename
from .category import Category
from ...common.models import BaseModel


path_name = PathAndRename('product')
class Product(BaseModel):
    name = models.CharField(max_length=255, unique=True, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(_('Slug'), blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to=path_name)
    quantity = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'product'
        db_name = 'product'
        verbose_name_plural = 'products'
        ordering = ['-date_joined']

    def __str__(self):
        return self.name
    def save(self):
        self.slug = slugify(self.name)
        super(Product, self).save()