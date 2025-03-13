from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("username", "email", "usertype", "department")
    list_filter = ("usertype", "department")
    search_fields = ("username", "email", "full_name", "id_number", "register_number")
    ordering = ("username",)

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal Info", {"fields": ("full_name", "email", "usertype", "id_number", "register_number")}),
        ("Academic Info", {"fields": ("semester", "department")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "usertype", "full_name", "id_number", "register_number", "semester", "department"),
        }),
    )

admin.site.register(User, CustomUserAdmin)
