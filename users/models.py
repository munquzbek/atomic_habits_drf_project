from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """Creating User model inherit only from AbstractUser"""
    username = None  # turn off login through username
    email = models.EmailField(unique=True, verbose_name='email')

    telegram_id = models.CharField(unique=True, max_length=32, verbose_name='telegram id', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='phone number', **NULLABLE)

    USERNAME_FIELD = "email"  # through what log in
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
