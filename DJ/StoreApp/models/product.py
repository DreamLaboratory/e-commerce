from django.db import models
# from django.translations import gettext_lazy
from ckeditor.fields import RichTextField
import sys
from .category import Category
from HomeApp.models import BaseModel
from django.urls import reverse
from HomeApp.file_renamer import PathAndRename
from django.utils.text import slugify
from django.db.models import Avg

sys.path.append("...")

path_and_rename = PathAndRename('products')


class Product(BaseModel):
    name = models.CharField(max_length=200, unique=True, db_index=True)
    slug = models.SlugField(max_length=200, unique=True, db_index=True, blank=True)
    descriptions = RichTextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to=path_and_rename)
    quantity = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True, help_text="Product Available")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    @property
    def get_absolute_url(self):
        return reverse("product_detail_view", args=[self.category.slug, self.slug])

    @property
    def average_rating(self):
        reviews = self.reviews.filter(status=True)
        reviews_average = self.reviews.filter(status=True).aggregate(Avg('rating'))
        reviews_count = reviews.count()
        if reviews_count > 0:
            average = reviews
            return "{:.2f}".format(reviews_average['rating__avg'])
        else:
            return '0'

    @property
    def get_image_url(self):
        return self.image.url if self.image and hasattr(self.image, 'url') else ""

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save()
