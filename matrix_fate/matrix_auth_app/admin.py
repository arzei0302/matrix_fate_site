from django.contrib import admin
from import_export.admin import ExportMixin

from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, EmailVerificationCode, Profile, UserCalculationHistory
from django.contrib import admin
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
## from rest_framework.authtoken.models import Token


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    search_fields = ('email',)
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'phone', 'created_at', 'avatar', 'access_level', 'access_expiration')
    search_fields = ('user__email', 'full_name', 'phone')
    list_filter = ('access_level', 'created_at')
    

# @admin.register(EmailVerificationCode)
# class EmailVerificationCodeAdmin(admin.ModelAdmin):
#     list_display = ('user', 'code', 'created_at')
#     search_fields = ('user__email', 'code')


@admin.register(UserCalculationHistory)
class UserCalculationHistoryAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('id', 'profile', 'category', 'input_data', 'created_at')
    search_fields = ('profile',)
    list_filter = ('id', 'profile', 'created_at', 'category')


admin.site.unregister(BlacklistedToken)
admin.site.unregister(OutstandingToken)
# admin.site.register(Token)
# admin.site.unregister(Token)