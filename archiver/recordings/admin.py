from django.contrib import admin

from .models import recordings


@admin.register(recordings)
class recordingsAdmin(admin.ModelAdmin):
    read_only_fields=['download_link']
    list_display = [
        'recording_tag',
        'download_link',
        'from_caller_id',
        'to_caller_id',
        'date_created_ts',
    ]
    
