from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import MyUserManager
from ..common.models import BaseModel


class MyUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(verbose_name="first name", max_length=30, blank=True, null=True)
    last_name = models.CharField(verbose_name="last name", max_length=30, blank=True, null=True)

    email = models.CharField(verbose_name="email", max_length=60, unique=True, db_index=True, null=True, blank=True)
    phone_number = models.CharField(max_length=40, null=True, blank=True, unique=True)
    username = models.CharField(max_length=30, unique=True)

    # phone_number = models.CharField(verbose_name='phone_number',max_length=30)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["username", "first_name"]

    objects = MyUserManager()

    def __str__(self):
        return str(self.email)

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True


class MyUserProfile(BaseModel):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="user_image")
    state = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)

    def __str__(self) -> str:
        return str(self.user.username)

    def full_address(self):
        return f"{self.adress} : {self.city}"
