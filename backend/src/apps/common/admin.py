# Register your models here.
from .models import SMSToken, SMSLog, City, Region
from django.contrib import admin
from django.contrib.auth.models import Group

admin.site.register([SMSLog, SMSToken, City, Region])

admin.site.unregister(Group)
admin.site.site_header = "Online Shop Admin Panel"
admin.site.site_title = "E-Commerce"
admin.site.site_url = "Fayzulloh"
admin.site.index_title = "Home Admin Panel"
admin.site.empty_value_display = "Mavjud emas"
