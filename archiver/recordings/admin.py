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
    list_filter = [
        'recording_tag',
        'from_caller_id',
        'to_caller_id',
        'date_created_ts',
    ]
    search_fields = [
        'recording_tag',
        'from_caller_id',
        'to_caller_id',
        'date_created_ts',
    ]
