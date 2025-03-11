from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

# Register your models here.
# admin.site.register(User)
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['email', 'first_name', 'last_name', "is_staff", 'public_id']

    search_fields = ['email','first_name', 'last_name']

    ordering = ['email']
    

    fieldsets = (
        (
            (None, {"fields": ("password",)})
        ),
        (

            ("Personale Info", {"fields": ('first_name', 'last_name', 'email')})
        ),
        (
            ("Permissions", {"fields": ('is_active',  'is_staff', 'is_superuser', 'groups', 'user_permissions')})
        ),
        (
            ("Imporatant Dates", {"fields": ("last_login",)})
        ),
        )
    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ("first_name","last_name" ,'email', 'password1', 'password2'),
        }),
    )
        
    