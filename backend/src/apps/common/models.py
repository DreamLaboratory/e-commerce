from django.db import models

# Create your models here.
from django.db import models


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class SMSToken(BaseModel):
    name = models.CharField(max_length=50)
    token = models.TextField()
    expires_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "SMS Token"
        verbose_name_plural = "SMS Tokens"
        ordering = ["-id"]


class SMSLog(BaseModel):
    phone = models.CharField(max_length=20)
    message = models.CharField(max_length=255)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = "SMS Log"
        verbose_name_plural = "SMS Logs"
        ordering = ["-id"]