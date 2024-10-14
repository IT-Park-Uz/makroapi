from django.contrib import admin

from common.ferma.models import Toys


@admin.register(Toys)
class ToysAdmin(admin.ModelAdmin):
    ...
