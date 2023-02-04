from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self,email,username,phone_number,password=None):
        if not email:
            raise ValueError('Email Does Not Exist')
        if not username:
            raise ValueError("username Does Not Exist")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            phone_number = phone_number
        )
        user.set_password(password)
        user.save(using = self._db)
        return user


    def create_superuser(self,email,username,phone_number,password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            username = username,
            phone_number = phone_number,
        )


        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user



class Account(AbstractBaseUser):
    first_name = models.CharField(verbose_name='first_name',max_length=30,null=True,blank=True)
    last_name = models.CharField(verbose_name='last_name',max_length=30,null=True,blank=True)
    email = models.CharField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    phone_number = models.CharField(verbose_name='phone_number',max_length=30,null=True,blank=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','phone_number']


    objects = MyAccountManager()

    def __str__(self):
        return self.email

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin


    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True


class Profile(models.Model):
    image = models.ImageField(null = True,blank = True)
    first_name = models.CharField(verbose_name = 'Name' , max_length = 202,null = True,blank = True)
    last_name = models.CharField(verbose_name = "Last Name",max_length = 200,null = True,blank = True)
    email = models.CharField(max_length = 30)
    user = models.OneToOneField(Account,on_delete = models.CASCADE ,null=True,blank=True)
    auth_token = models.CharField(max_length = 200)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.email



