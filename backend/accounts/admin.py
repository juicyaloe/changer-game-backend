from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
from .forms import UserChangeForm, UserCreationForm
from .models import User

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    readonly_fields = ["created_at", "updated_at"]

    list_display = ('userid', 'name', 'address', 'phone', 'phone_check',
                    'email', 'email_check', 'date_of_birth', 'level', 'recommendation', 'account', 'is_admin',
                    'created_at', 'updated_at')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('userid', 'password')}),
        ('Personal info', {'fields': ('name', 'address', 'phone', 'phone_check',
                                      'email', 'email_check', 'date_of_birth', 'level', 'recommendation', 'account')}),
        ('date', {'fields': ('created_at', 'updated_at')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('userid', 'name', 'address', 'phone', 'phone_check', 'email', 'email_check',
                       'date_of_birth', 'level', 'recommendation', 'account', 'password1', 'password2')}
         ),
    )

    search_fields = ('userid',)
    ordering = ('userid',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
