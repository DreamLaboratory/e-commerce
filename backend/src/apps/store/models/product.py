from django.db import models
from ...common.models import BaseModel
from django.utils.translation import gettext_lazy as _
from ...common.file_renamer import PathAndRename
from .category import Category
from django.utils.text import slugify

# Create your models here.
file_rename_class = PathAndRename("product_images")


class Product(BaseModel):
    name = models.CharField(max_length=255, unique=True, db_index=True)
    description = models.TextField(max_length=1000, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=3)  # how to have different max_digits and max_length
    slug = models.SlugField(
        _("Slug"), unique=True, db_index=True, max_length=500, blank=True
    )  # what to do gettext_lazy
    image = models.ImageField(upload_to=file_rename_class)
    stock = models.PositiveIntegerField(default=0)
    is_availabel = models.BooleanField(default=True, help_text="is product available?")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        # db_name='Product'
        ordering = ["-created_date"]

    def save(self):
        self.slug = slugify(self.name)
        super(Product, self).save()

    def __str__(self):
        return self.name
