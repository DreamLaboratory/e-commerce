from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .account_manager import UserManager


# Accounts
class User(AbstractBaseUser, PermissionsMixin):
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(
        max_length=50, unique=True, blank=True, null=True)

    # talab qilinadi
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"  # username

    REQUIRED_FIELDS = ['username', 'phone_number']

    objects = UserManager()

    def __str__(self) -> str:
        return self.phone_number

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to="profile_pics", default="profile_pics/default.png")
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.first_name

    def full_address(self):
        return f"{self.address_1}"

    class Meta:
        verbose_name = _("UserProfile")
        verbose_name_plural = _("UserProfiles")
        ordering = ["-id"]
