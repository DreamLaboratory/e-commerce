from django.db import models

class VariantCategory(models.TextChoices):
    SIZE='size'
    COLOR='color'

class VariantValueColor(models.TextChoices):
    COLOR=('red','blue','green')
class VariantValueSize(models.TextChoices):
    SIZE=('S','M','L','XL')