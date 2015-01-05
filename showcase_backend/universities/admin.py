from django.contrib import admin

from .models import University


class UniversityAdmin(admin.ModelAdmin):
    list_display = (u'id', 'name', 'emblem', 'town')
    search_fields = ('name',)

admin.site.register(University, UniversityAdmin)
