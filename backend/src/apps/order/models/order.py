from django.db import models
from ...common.models import BaseModel
from ...cart.models import CartItem
from django.contrib.auth import get_user_model
from ..choose import OrderStatus
from smart_selects.db_fields import ChainedForeignKey
from ...common.models import Region, City

User = get_user_model()


class Order(BaseModel):
    order_number = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_items = models.ManyToManyField(CartItem, related_name="orders")
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    cities = ChainedForeignKey(
        City,
        chained_field="region",
        chained_model_field="region",
        show_all=False,
        auto_choose=True,
        sort=True,
        on_delete=models.SET_NULL,
        null=True,
    )

    address = models.CharField(max_length=255)
    order_note = models.TextField(blank=True, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    ip = models.GenericIPAddressField(max_length=255)
    status = models.CharField(max_length=30, choices=OrderStatus.choices, default=OrderStatus.NEW)
    first_name = models.CharField(max_length=255)

    def get_full_name(self) -> str:
        return f"{self.first_name}  :  {self.last_name}"

    def __str__(self):
        return f"{self.user} "

    class Meta:
        ordering = ["-created_date"]
