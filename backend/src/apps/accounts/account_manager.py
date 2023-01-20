from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, email, phone_number, password=None):

        if not email:
            raise ValueError("Userda Email bulishi shart")

        if not username:
            raise ValueError("Userda username bulishi kerak")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          phone_number=phone_number)
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, phone_number, password=None):
        user = self.create_user(
            email=email, username=username, phone_number=phone_number, password=password)

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user
