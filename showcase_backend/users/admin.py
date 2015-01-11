from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as DJUserAdmin

from .models import User
from .forms import UserCreationForm, UserChangeForm


class UserAdmin(DJUserAdmin, admin.ModelAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = (
        u'id',
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

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name',
                                      'university', 'department',
                                      )}),
        ('Permissions', {'fields': ('is_active', 'is_superuser',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',
                       'university', 'department')
        }
        ),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
