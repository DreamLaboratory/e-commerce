from django.contrib import admin
from .models import MyUser, MyUserProfile
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html


# Register your models here.
class MyUserAdmin(UserAdmin):
    list_display = ("username", "email", "is_staff", "is_active", "phone_number")
    list_filter = ("is_staff", "is_active", "phone_number")
    list_display_links = ("username", "email")
    readonly_fields = ("date_joined", "last_login")
    filter_horizontal = ("groups", "user_permissions")
    list_editable = ["phone_number", "is_active"]
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
    list_display = ["show_profile_image", "user", "city", "address", "state"]
    list_filter = ["state", "city"]
    list_display_links = ["user", "city", "state", "address"]

    def show_profile_image(self, object):
        if object.image:
            return format_html(f'<img src="{object.image.url}" width="40" style="border-radius: 50px;" />')
        else:
            return format_html('<b style="color:red;">not fount profile image </b>')

    show_profile_image.short_description = "Profile Image"

    def set_defoult(self, request, queryset):
        queryset.update(city="qashqadaryo")

    set_defoult.short_description = "set_defoult_all"

    actions = ["set_defoult"]


admin.site.register(MyUserProfile, MyuserProfileAdmin)
