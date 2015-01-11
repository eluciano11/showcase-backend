from django.contrib import admin

from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        u'id',
        'created_by',
        'created_at',
        'title',
        'summary',
        'story',
        'screenshot',
    )
    list_filter = ('created_by', 'created_at')
    search_fields = ('title', )
    date_hierarchy = 'created_at'

admin.site.register(Project, ProjectAdmin)
