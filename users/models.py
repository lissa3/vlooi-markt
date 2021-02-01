from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractUser

from users.managers import CustomUserManager
from proj_help.help_utils import upload_to


class User(AbstractUser):
    """
    username + email for signup; email for login;
    user should choose at the moment of signUp one of two options:
    is_customer or is employee;
    admin/staff members could keep default values;
    """
    username = models.CharField(_("Username"), unique=True, max_length=120)
    email = models.EmailField(_("Email"), unique=True)
    avatar = models.ImageField(_("Avatar"), upload_to=upload_to, blank=True)
    banned = models.BooleanField(default=False)
    blackListEmail = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.username
