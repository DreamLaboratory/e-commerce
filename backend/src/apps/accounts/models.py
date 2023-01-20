from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .manager import MyUserManager



class MyUser(AbstractBaseUser,PermissionsMixin):
    first_name = models.CharField(verbose_name='first name',max_length=30,blank=True,null=True)
    last_name = models.CharField(verbose_name='last name',max_length=30,blank=True,null=True)

    email = models.CharField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)

    # phone_number = models.CharField(verbose_name='phone_number',max_length=30)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyUserManager()

    def str(self):
        return self.email

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin


    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

