from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, shipping_address='111', phone_number='111', **extra_fields):
        if not username:
            raise ValueError('The username field must be set')
        if not password:
            raise ValueError('The password field must be set')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, shipping_address=shipping_address, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, shipping_address='111', phone_number='111', **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, shipping_address, phone_number,**extra_fields)


