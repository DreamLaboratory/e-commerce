from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, phone_number, password=None):

        if not phone_number:
            raise ValueError("Userda phone_number address bulishi shart")

        if not username:
            raise ValueError("Usern username bulishi kerak")

        user = self.model(phone_number=phone_number, username=username, first_name=first_name, last_name=last_name)
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, phone_number, username, password=None):
        user = self.create_user(
            phone_number=phone_number, username=username, first_name=first_name, last_name=last_name, password=password
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user
