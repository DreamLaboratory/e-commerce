from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, Profile
from django.utils.html import format_html
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class ResourceAccount(resources.ModelResource):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email', 'username', 'phone_number', 'is_admin')


@admin.register(Account)
class AccountAdmin(UserAdmin,ImportExportModelAdmin):
    resource_class = ResourceAccount
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')
    list_display = ('phone_number', 'date_joined', 'last_login', 'is_admin', 'is_staff', 'is_active')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


    class Meta:
        model = Account
        fields = ('email', 'username', 'is_staff')


@admin.register(Profile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('image_profile', 'phone_number', 'email', 'address', 'is_verified')
    list_filter = ('email', 'address', 'is_verified')
    list_display_links = ('email', 'address','phone_number', 'is_verified')

    def image_profile(self, object):
        if object.image:
            return format_html(
                f'<img src="{object.image.url}" width="45px" height="45px" style="border-radius: 45px;" />'
            )
        else:
            return format_html(
                '<img src="https://www.kindpng.com/picc/m/24-248253_user-profile-default-image-png-clipart-png-download.png" width="40" style="border-radius: 50px;" />'
            )

    image_profile.short_description = 'Profile Image'

    def set_default_city(self, request, queryset):
        queryset.update(address='This profile is not address')

    set_default_city.short_description = 'Default add address'

    def verify_check(self, request, queryset):
        queryset.update(is_verified=True)

    verify_check.short_description = 'All verify change True'

    def default_name(self, request, queryset):
        queryset.update(first_name='this Profile is not name')

    default_name.short_description = 'Default None name'

    actions = ['set_default_city', 'verify_check', 'default_name']
