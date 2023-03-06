from django.contrib import admin
from .models import BaseModel, SMSToken, SMSLog, City, Region
from django.contrib.auth.models import Group

admin.site.unregister(Group)
admin.site.site_header = 'Online Shop Admin Panel'
admin.site.site_title = "E-Commerce"
admin.site.index_title = 'MarketPlace'
admin.site.empty_value_display = 'Mavjud Emas'

admin.site.register(SMSToken)
admin.site.register(SMSLog)
admin.site.register(Region)
admin.site.register(City)
