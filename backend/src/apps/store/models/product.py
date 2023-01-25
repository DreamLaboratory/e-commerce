from django.db import models
from django.utils.text import slugify

from ...common.models import BaseModel
from ...common.file_renamer import PathAndRename
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from .category import Category

path_and_rename = PathAndRename("products")


# Create your models here.
class Product(BaseModel):
    name = models.CharField(max_length=255, unique=True, db_index=True)
    slug = models.SlugField(_("Slug"), max_length=255, unique=True, db_index=True, blank=True)
    description = RichTextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to=path_and_rename)
    stock = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True, help_text="Is product available?")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def save(self):
        self.slug = slugify(self.name)
        super(Product, self).save()
