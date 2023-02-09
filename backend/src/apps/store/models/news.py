from ...common.models import BaseModel
from django.db import models


class News(BaseModel):
    name = models.CharField(max_length=10)
