from django.contrib import admin

from .models import City, Region
from django.contrib.auth.models import Group  # noqa


# Admin Navbar
# Remove group from admin page
admin.site.unregister(Group)
admin.site.site_header = "Online Shop Admin Panel"
admin.site.site_title = "E-Commerce"
admin.site.index_title = "MarketPlace"
admin.site.empty_value_display = "Mavjud emas"


admin.site.register(Region)
admin.site.register(City)
