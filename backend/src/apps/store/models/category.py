from ...common.models import BaseModel
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Category(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    description = RichTextField(max_length=255, blank=True)  # TODA: richTExtFields qilish
    image = models.ImageField(upload_to="category_images", null=True, blank=True)
    slug = models.SlugField(_("Slug"), db_index=True, max_length=1000, unique=True, blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        # db_name='Category'
        ordering = ["-created_date"]

    def save(self):
        self.slug = slugify(self.name)
        super(Category, self).save()

    def __str__(self):
        return self.name
