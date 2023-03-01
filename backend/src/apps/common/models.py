from django.db import models


class BaseModel(models.Model):
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Region(BaseModel):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'
    def __str__(self) -> str:
        return self.name
    
class City(BaseModel):
    name = models.CharField(max_length=30, blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self) -> str:
        return self.name