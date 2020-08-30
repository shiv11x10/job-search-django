from django.contrib import admin
from .models import Job


class JobAdmin(admin.ModelAdmin):
    list_display = [
        'type',
        'created_at',
        'company',
        'location',
        'title',
    ]


admin.site.register(Job, JobAdmin)
