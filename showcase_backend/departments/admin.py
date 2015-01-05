from django.contrib import admin

from .models import Department


class DepartmentAdmin(admin.ModelAdmin):
    list_display = (u'id', 'name')
    list_filter = ('name',)
    search_fields = ('name',)


admin.site.register(Department, DepartmentAdmin)
