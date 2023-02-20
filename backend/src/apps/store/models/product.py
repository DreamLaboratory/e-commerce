from django.db import models
from ...common.models import BaseModel
from django.utils.translation import gettext_lazy as _
from ...common.file_renamer import PathAndRename
from .category import Category
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.db.models import Avg, Count


# Create your models here.
file_rename_class = PathAndRename("product_images")


class Product(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categories", null=True,blank=True)
    name = models.CharField(max_length=255, unique=True, db_index=True)
    description = RichTextField(max_length=255, blank=True)  # TODA: richTExtFields qilish

    price = models.DecimalField(max_digits=10, decimal_places=3)  # how to have different max_digits and max_length
    slug = models.SlugField(
        _("Slug"), unique=True, db_index=True, max_length=500, blank=True
    )  # what to do gettext_lazy
    image = models.ImageField(upload_to=file_rename_class, blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    is_availabel = models.BooleanField(default=True, help_text="is product available?")

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        # db_name='Product'
        ordering = ["-created_date"]

    def __str__(self):
        return self.name

    @property
    def get_absolute_url(self):
        return reverse("store:product_list_view", args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save()

    @property
    def get_image_url(self):
        return self.image.url if self.image and hasattr(self.image, "url") else "#"

    @property
    def average_rating(self):

        reviews = self.reviews.filter().aggregate(Avg("rating"))

        return float(reviews["rating__avg"] if reviews["rating__avg"] else 0)

    @property
    def get_absolute_url(self):
        return reverse("store:product_detail_view", args=[self.category.slug, self.slug])

    @property
    def get_view_count(self):
        reviews = self.reviews.all().aggregate(count=Count("desc"))
        return int(reviews["count"] if reviews["count"] else 0)
