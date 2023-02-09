from django.contrib import admin
from .models import MyUser, MyUserProfile
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class MyUserAdmin(UserAdmin):
    list_display = ("username", "email", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")
    list_display_links = ("username", "email")
    readonly_fields = ("date_joined", "last_login")
    filter_horizontal = ("groups", "user_permissions")
    fieldsets = (
        ("Personal Info", {"fields": ("username", "email", "password")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "first_name",
                    "email",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )

    class Meta:
        model = MyUser


admin.site.register(MyUser, MyUserAdmin)


class MyuserProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "city", "address", "state"]
    list_filter = ["state", "city"]
    list_display_links = ["user", "city", "state", "address"]


admin.site.register(MyUserProfile, MyuserProfileAdmin)
