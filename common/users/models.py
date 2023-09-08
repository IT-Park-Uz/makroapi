from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.users.base import BaseModel


class User(AbstractUser, BaseModel):
    first_name = None
    last_name = None
    name = models.CharField(_("Name of User"), max_length=100)

    def __str__(self):
        return "USER:" + ' ' + str(self.username)
