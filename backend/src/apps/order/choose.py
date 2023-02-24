from django.db import models


class OrderStatus(models.TextChoices):
    NEW = "NEW"
    CANCELED = "CANCELED"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"
