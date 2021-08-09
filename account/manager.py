from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Custom User model manager where email is the unique identifier
    for auth instead of username.
    """

    def create_user(self, email, password, name=None, **kwargs):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('Email Address Must be Set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)

        if name:
            user.name = name
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        """
        Create and save a SuperUser with the given email and password.
        """
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError(_('SuperUser Must have is_staff = True'))
        if kwargs.get('is_superuser') is not True:
            raise ValueError(_('SuperUser Must have is_superuser = True'))

        return self.create_user(email, password, **kwargs)
