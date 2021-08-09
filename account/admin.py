from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.models import LogEntry

from account.models import CustomUser

admin.site.site_header = 'This is Business!!!'
admin.site.index_title = 'Business Admin'


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    Configuration for User in DjangoAdmin
    """
    model = CustomUser
    list_display = (
        "name",
        "email",
        "created_at",
        "is_staff",
        "is_active",
        "is_superuser",
    )
    list_filter = (
        "is_staff",
        "is_active",
    )

    """
    CustomUserChangeForm fields
    """
    fieldsets = (
        ("Information", {"fields": ("name", "email", "password")}),
        ("Permissions", {
            "fields": (
                "is_staff",
                "is_active",
                'is_superuser',
                'groups',
                'user_permissions',
            )
        }),
    )

    """
    CustomUserCreationForm fields
    """
    add_fieldsets = (
        (
            "Information",
            {
                "classes": ("wide",),
                "fields": (
                    "name",
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = (
        "name",
        "email",
    )
    ordering = [
        "-created_at",
    ]


class MonitorLog(admin.ModelAdmin):
    list_display = (
        'user', 'action_time', 'content_type',
        'object_repr', 'get_change_message', 'get_edited_object',
        'action_flag', 'get_admin_url'
    )

    ordering = ('-action_time',)


admin.site.register(LogEntry, MonitorLog)
