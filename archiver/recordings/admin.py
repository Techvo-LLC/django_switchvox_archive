from django.contrib import admin
from rangefilter.filter import DateRangeFilter
from .models import recordings


@admin.register(recordings)
class recordingsAdmin(admin.ModelAdmin):
    
    list_display = [
        'recording_tag',
        'from_caller_id',
        'to_caller_id',
        'duration',
        'date_created_ts',
        'audio_player',
        'download_link',
    ]
    list_filter = (
        ('date_created_ts', DateRangeFilter),
        'recording_tag',
        'from_caller_id',
        'to_caller_id',
    )
    search_fields = [
        'recording_tag',
        'from_caller_id',
        'to_caller_id',
        'date_created_ts',
    ]
    readonly_fields=['download_link', 'audio_player']
    
    fieldsets = (
        (None, {
            "fields": (
                'audio_player',
                'date_created_ts',
                'from_caller_id',
                'to_caller_id',
            ),
        }),
    )
    