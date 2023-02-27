from ...common.models import BaseModel
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

from django.urls import reverse


class Category(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(_('Slug'), unique=True, blank=True)
    image = models.ImageField(upload_to='category', blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ["-date_joined"]

    def __str__(self):
        return self.name

    @property
    def get_absolute_url(self):
        return reverse('store:product_list_view', args=[self.slug])

    def save(self):
        self.slug = slugify(self.name)
        super(Category, self).save()
