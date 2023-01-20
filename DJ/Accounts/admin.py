from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin(UserAdmin):
    search_fields = ('email','username')
    readonly_fields = ('date_joined','last_login')
    list_display = ('email', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


    class Meta:
        model = Account
        fields = ('email','username','is_staff')

admin.site.register(Account,AccountAdmin)



