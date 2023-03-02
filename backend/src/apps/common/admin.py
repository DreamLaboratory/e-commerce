# Register your models here.
from .models import SMSToken,SMSLog,City,Region
from django.contrib import admin


admin.site.register([SMSLog,SMSToken,City,Region])