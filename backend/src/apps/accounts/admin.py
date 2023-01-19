# Register your models here.
from .models import Account, UserProfile
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "phone_number", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")
    list_display_links = ("username", "email", "phone_number")
    filter_horizontal = ("groups", "user_permissions")
    readonly_fields = ("date_joined", "last_login")
    fieldsets = (
        ("Personal Info", {"fields": ("username", "email", "phone_number", "password")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "phone_number", "password1", "password2"),
        }),
    )


admin.site.register(Account, CustomUserAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "city", "state", "address")
    list_filter = ("city", "state")
    list_display_links = ("user", "city", "state")


admin.site.register(UserProfile, UserProfileAdmin)