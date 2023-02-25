from django.contrib.auth import get_user_model
from django.db import models
from HomeApp.models import BaseModel
from Cart.models import CartItems

User = get_user_model()


class OrderStatus(models.TextChoices):
    NEW = "NEW", 'new'
    IN_PROGRESS = "IN_PROGRESS", 'in_progress'
    DONE = "DONE", 'done'
    CANCELED = "CANCELED", 'canceled'


class Order(BaseModel):
    order_number = models.CharField(max_length=40, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_orders')
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    regions = models.CharField(max_length=255)
    city = models.CharField(max_length=255)  # TODO Model City
    address = models.CharField(max_length=255)
    order_note = models.TextField(blank=True, null=True)  # TODO RichTextField
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    ip = models.CharField(max_length=255)
    status = models.CharField(max_length=200, choices=OrderStatus.choices, default=OrderStatus.NEW)
    cart_items = models.ManyToManyField(CartItems, related_name='orders')

    def __str__(self):
        return f"{self.user}"

    @property
    def get_full_name(self):
        return f"{self.f_name} - {self.l_name}"

    class Meta:
        ordering = ['-created_at']
