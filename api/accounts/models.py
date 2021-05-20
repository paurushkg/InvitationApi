from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
)


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, is_staff=False, is_admin=False, is_active=True):
        if not phone_number:
            raise ValueError('User must have phone number')
        if not password:
            raise ValueError('User must have password')
        user = self.model(
             phone_number=phone_number
         )
        user.set_password(password)
        user.staff = is_staff
        user.admin = is_admin
        user.active = is_active

        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password):
        user = self.create_user(
            phone_number,
            password=password,
            is_staff=True,
            is_admin=True,
        )
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=10, unique=True)
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=True)
    staff = models.BooleanField(default=True)

    USERNAME_FIELD = 'phone_number'

    objects = UserManager()

    def __str__(self):
        return self.phone_number

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_admin(self):
        return self.is_admin
