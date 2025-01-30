from django.db import models


class Offerta(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок")
    file = models.FileField(verbose_name="Файл", upload_to='offerta', null=True, blank=True)

    def __str__(self):
        return f"{self.title}"
