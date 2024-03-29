from django.db import models
from django.db.models import Avg, Count
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from ...common.file_renamer import PathAndRename
from ...common.models import BaseModel
from .category import Category

# products/file_{id}_{hex4}.{ext}
path_and_rename = PathAndRename("products")

# Product model
class Product(BaseModel):
    name = models.CharField(
        max_length=255, unique=True, verbose_name=_("Name"), help_text=_("Product name"), null=True, blank=True
    )
    slug = models.SlugField(_("Slug"), max_length=255, unique=True, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    image = models.ImageField(upload_to=path_and_rename, blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True, help_text="Is product available?")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", blank=True, null=True)

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"
        ordering = ["-created_at"]

    @property
    def get_absolute_url(self):
        return reverse("store:product_detail_view", args=[self.category.slug, self.slug])

    def __str__(self):
        return str(self.name)

    @property
    def get_image_url(self):
        return self.image.url if self.image and hasattr(self.image, "url") else "#"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save()

    # TODO fix 3.3333333333333335
    @property
    def average_rating(self):
        reviews = self.reviews.filter(status=True).aggregate(Avg("rating"))
        return float(reviews["rating__avg"]) if reviews["rating__avg"] else 0

    @property
    def get_review_count(self):
        reviews = self.reviews.filter(status=True).aggregate(count=Count("rating"))
        return reviews["count"]


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to=path_and_rename)

    @property
    def get_image_url(self):
        return self.image.url if self.image and hasattr(self.image, "url") else "#"

    class Meta:
        verbose_name = "Product image"
        verbose_name_plural = "Product images"
        ordering = ["-created_at"]

    def __str__(self):
        return str(self.product)
