from django.contrib import admin

from .models import BaseModel,SMSToken,SMSLog
admin.site.register(SMSToken)
admin.site.register(SMSLog)



