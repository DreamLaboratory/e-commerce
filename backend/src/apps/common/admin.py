# Register your models here.
from .models import SMSToken,SMSLog
from django.contrib import admin


admin.site.register([SMSLog,SMSToken ])