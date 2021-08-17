from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import User
# Register your models here.
@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    list_display = (
        'username',
        'date_joined',
        'email',
        'is_staff',
        'is_active',
    )
    sortable_by = ['username', 'date_joined']
    list_editable = ['is_staff', 'is_active']
    search_fields = ['first_name', 'last_name', 'username', 'email']
    readonly_fields = ['date_joined', 'last_login']