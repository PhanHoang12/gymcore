from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,MemberProfile

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Thông tin GymCore", {
            "fields": ("role",),
        }),
    )
    list_display = (
        "username",
        "email",
        "role",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "role",
        "is_staff",
        "is_active",
    )
    search_fields = (
        "username",
        "email"
    )
@admin.register(MemberProfile)
class MemberProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "phone",
        "join_date",
    )

    search_fields = (
        "user__username",
        "user__email",
        "phone",
    )
# Register your models here.
