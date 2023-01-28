from django.db import models
# from django.translations import gettext_lazy
import sys
from .category import Category
from HomeApp.models import BaseModel
from HomeApp.file_renamer import PathAndRename
from django.utils.text import slugify
sys.path.append("...")



path_and_rename = PathAndRename('products')

class Product(BaseModel):
    name = models.CharField(max_length = 200,unique = True,db_index = True)
    slug = models.SlugField(max_length = 200,unique = True,db_index = True,blank =True)
    descriptions = models.TextField(max_length = 1000,blank = True)
    price = models.DecimalField(max_digits = 10,decimal_places = 2)
    image = models.ImageField(upload_to = path_and_rename)
    quantity = models.PositiveIntegerField()
    is_available = models.BooleanField(default = True,help_text = "Product Available")
    category = models.ForeignKey(Category,on_delete = models.CASCADE)


    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ['-created_at']


    def __str__(self):
        return self.name

    def save(self):
        self.slug = slugify(self.name)
        super(Product,self).save()