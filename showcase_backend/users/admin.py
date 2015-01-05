from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        u'id',
        'password',
        'last_login',
        'first_name',
        'last_name',
        'email',
        'gravatar_url',
        'university',
        'department',
        'is_staff',
        'is_superuser',
        'is_active',
    )
    list_filter = (
        'last_login',
        'university',
        'department',
        'is_staff',
        'is_superuser',
        'is_active',
    )

admin.site.register(User, UserAdmin)
