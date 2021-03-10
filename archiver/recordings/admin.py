from django.contrib import admin
from .models import recordings


@admin.register(recordings)
class recordingsAdmin(admin.ModelAdmin):
    pass

