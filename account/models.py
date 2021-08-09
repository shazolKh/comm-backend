import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from account.manager import CustomUserManager


# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_('Name'), max_length=50, null=True, blank=True)
    email = models.EmailField(_('Email Address'), max_length=255, unique=True)
    created_at = models.DateTimeField(_('Joined'), auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('Custom User')
        verbose_name_plural = _('Custom Users')

    def __str__(self):
        return f'{self.email}, {self.name}'
