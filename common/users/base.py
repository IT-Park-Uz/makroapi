import uuid

from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    guid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class BaseMeta(object):
    ordering = ["-id"]
