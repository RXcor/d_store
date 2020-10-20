from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import CustomUserManager
from app.models import Role

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    last_name = models.CharField(verbose_name="Фамилия", max_length=40, blank=True)
    first_name = models.CharField(verbose_name="Имя", max_length=40, blank=True)
    middle_name = models.CharField(verbose_name="Отчество", max_length=40, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    delivery_address = models.CharField(verbose_name="Адрес доставки", max_length=50, blank=True)
    role = models.ForeignKey('app.Role', verbose_name="Роль", null=True, on_delete=models.SET_NULL)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    def __str__(self):
        return self.email
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)


# Create your models here.
