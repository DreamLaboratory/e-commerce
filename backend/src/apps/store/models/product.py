from django.utils.text import slugify
from django.db import models
from django.utils.translation import gettext_lazy as _

from ...common.renamed import PathAndRename
from .category import Category
from ...common.models import BaseModel

from django.urls import reverse

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
        # db_name = 'product'
        verbose_name_plural = 'products'
        ordering = ['-date_joined']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:product_detail_view', args=[self.category.slug, self.slug])

    @property
    def average_rate(self):
        from ..models.review import Review
        reviews = Review.objects.filter(product=self)
        review_count = reviews.count()
        average = 0
        if review_count > 0:
            average = sum(rereview.rate for rereview in reviews) / review_count
            return round(average, 2)

    def save(self):
        self.slug = slugify(self.name)
        super(Product, self).save()


class Product_Image(BaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_image')
    images = models.ImageField(upload_to=path_name)

    class Meta:
        verbose_name = 'Product_Image'
        verbose_name_plural = "Product_Images"

    # def get_image_url(self):
    # if self.image and hasattr(self.images, 'url'):
    #     return self.image.url

    def __str__(self) -> str:
        return self.product.name
