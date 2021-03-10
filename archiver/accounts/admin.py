from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from .models import CustomUser

# actions
def activate(modeladmin, request, queryset):
    queryset.update(is_active=True)
activate.short_description = 'Activate User'

def deactivate(modeladmin, request, queryset):
    queryset.update(is_active=False)
deactivate.short_description = 'Deactivate User'


# User Model
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['full_name','email','is_active','is_staff']
    actions = [activate, deactivate]

    fieldsets = (
        (None, {
            "fields": (
                ('first_name', 'last_name',),
                'email',
            )
        }),
        ('User Elevation', {
            "fields": (
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
    )