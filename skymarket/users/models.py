from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from .managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class UserRoles(models.TextChoices):
    USER = 'user', _('user')  # Пользователь
    ADMIN = 'admin', _('admin')  # Админ


class User(AbstractBaseUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'role']  # # 'role'

    objects = UserManager()

    first_name = models.CharField('Имя', max_length=40)
    last_name = models.CharField('Фамилия', max_length=60)
    phone = PhoneNumberField('Телефон', unique=True)
    email = models.EmailField('Электронная почта', unique=True)
    role = models.CharField('Роль', max_length=5, choices=UserRoles.choices, default=UserRoles.USER,
                            help_text='Выберите роль')
    image = models.ImageField('Аватарка', upload_to='avatars', blank=True, null=True)
    is_active = models.BooleanField('Действующий', default=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
