from django.db import models


class Toys(models.Model):
    picture = models.ImageField(upload_to="ferma")
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    role = models.CharField(max_length=255)
    facts = models.CharField(max_length=500)

    def __str__(self):
        return self.name
