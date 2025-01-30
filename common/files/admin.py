from django.contrib import admin

from .models import Offerta


@admin.register(Offerta)
class OffertaAdmin(admin.ModelAdmin):
    list_display = ['title']
