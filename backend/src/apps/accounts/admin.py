from django.contrib import admin
from .models import MyUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class MyUserAdmin(UserAdmin):
    search_fields = ('email','username')
    readonly_fields = ('date_joined','last_login')
    list_display = ('email', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


    class Meta:
        model = MyUser

admin.site.register(MyUser,MyUserAdmin)