# import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserManager


class User(AbstractUser):
    first_name = models.CharField(max_length=100, verbose_name="Ism")
    last_name = models.CharField(max_length=100, verbose_name="Familiya")
    username = models.CharField(max_length=100, blank=True, verbose_name="Username")
    email = models.CharField(max_length=100, unique=True, verbose_name="E-mail manzil")
    profile_image = models.ImageField(
        upload_to='images/', default='images/profile_image.png', null=True, blank=True, verbose_name="Profil rasmi")
    is_staff = models.BooleanField(default=False, verbose_name="Xodimlik statusi")
    is_superuser = models.BooleanField(default=False, verbose_name="Superuser statusi")
    is_active = models.BooleanField(default=True, verbose_name="Akkauntning faollik statusi")
    objects = UserManager()

    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']
    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f'{self.first_name} {self.last_name}'