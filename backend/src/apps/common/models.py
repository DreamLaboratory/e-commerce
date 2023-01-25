from django.db import models


class BaseModel(models.Model):
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
