from ..command_auto.create_product import Command
from django.db import models
from ...accounts.models import MyUser
from .product import Product

class Reviews(Command):
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    ip=models.GenericIPAddressField()
    desc=models.TextField()
    status=models.BooleanField(default=False)
    rating=models.IntegerField(default=0)
    reply=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name='Review'
        verbose_name_plural='Reviews'
        # ordering=['-created_date']

# TODO: centray: xato chiqsa emailga borib turish

 
