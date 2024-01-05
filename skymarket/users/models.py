from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models

from .managers import CustomUserManager

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    ROLE = [
        ('user', 'Пользователь'),
        ('admin', 'Администратор')
    ]

    username = None

    email = models.EmailField(unique=True, verbose_name='Почта', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    first_name = models.CharField(max_length=150, verbose_name='Имя пользователя', **NULLABLE)
    last_name = models.CharField(max_length=150, verbose_name='Фамилия пользователя', **NULLABLE)
    image = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    role = models.CharField(max_length=20, choices=ROLE, verbose_name='Роль пользователя', **NULLABLE)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
