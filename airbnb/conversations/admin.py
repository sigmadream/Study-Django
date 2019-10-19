from django.contrib import admin
from . import models


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Converstation)
class ConverstationAdmin(admin.ModelAdmin):
    pass

