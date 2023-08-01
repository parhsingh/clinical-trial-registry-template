from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, Organisation, PrimaryRegistry, SecondaryRegistry

from django.core.mail import send_mail
from django.conf import settings

class CustomUserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'mobile_number', 'gender', 'organisation', 'designation')}),
        ('Approval', {'fields': ('access',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'access')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)

    # Notification Mail for Access Approval
    def save_model(self, request, obj, form, change):
         original_obj = self.model.objects.get(pk=obj.pk) if change else None

         if original_obj and not original_obj.access and obj.access:
             subject = 'CTR: Access Granted'
             message = f'Dear {obj.first_name} {obj.last_name},\nYour access has been approved! You are now allowed to register clinical trials on the behalf of your organisation: {obj.organisation}.\n\nRegards,\nTeam CTR, ICMR'
             from_email = settings.DEFAULT_FROM_EMAIL
             recipient_list = [obj.email]
             send_mail(subject, message, from_email, recipient_list)
	
             super().save_model(request, obj, form, change)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Organisation)
admin.site.register(PrimaryRegistry)
admin.site.register(SecondaryRegistry)