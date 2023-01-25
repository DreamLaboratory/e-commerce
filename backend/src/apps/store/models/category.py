from ...common.models import BaseModel
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
class Category(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(_('Slug'), unique=True, blank=True)
    image = models.ImageField(upload_to='category')
    description = models.TextField(max_length=1000, blank=True, null=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        db_name = 'category'
        ordering = ["-date_joined"]

    def __str__(self):
        return self.name

    def save(self):
        self.slug = slugify(self.name)
        super(Category, self).save()
