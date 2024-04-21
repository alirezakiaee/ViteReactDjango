from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), max_length=255, unique=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=False)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()
    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.email
    
    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"