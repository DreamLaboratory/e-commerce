from django.db import models


class StatusChoices(models.TextChoices):
    ACTIVE = "active"
    INACTIVE = "inactive"
