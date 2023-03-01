from ..common.models import BaseModel
from django.db import models
from ..cart.models import CartItem

from django.contrib.auth import get_user_model
from smart_selects.db_fields import ChainedForeignKey
# Create your models here.
from ..common.models import City, Region
User = get_user_model()
class OrderStatus(models.TextChoices):
    NEW = "NEW"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"
    CANCELED = "CANCELED"

class Order(BaseModel):
    order_number = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    regions = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    city = ChainedForeignKey(City, chained_field='regions', chained_model_field='regions', auto_choose=True, show_all=False, sort=True, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=40)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_note = models.TextField(blank=True, null=True)
    ip = models.CharField(max_length = 50, blank=True, null=True)
    status = models.CharField(max_length=30, choices=OrderStatus.choices, default=OrderStatus.NEW)
    cart_items = models.ManyToManyField(CartItem, related_name='orders')

    class Meta:
        ordering= ['-date_joined']
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
    
    def __str__(self) -> str:
        return self.order_number
    
    @property
    def get_full_name(self):
        return f"{self.l_name} - {self.f_name}"
    


