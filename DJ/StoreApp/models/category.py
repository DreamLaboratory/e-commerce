from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy
import sys
sys.path.append("...")

from HomeApp.models import BaseModel



class Category(BaseModel):
    name = models.CharField(max_length =40, unique = True)
    slug = models.SlugField(max_length = 100,unique = True ,blank = True)
    descriptions = models.TextField(max_length = 355,blank =True)
    image = models.ImageField(upload_to = 'categories')

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def save(self):
        self.slug = slugify(self.name)
        super(Category,self).save()

