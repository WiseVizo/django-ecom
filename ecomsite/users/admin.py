from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import CustomUser  # Import your custom user model

# Define your custom UserAdmin class
class CustomUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'shipping_address', 'phone_number')

# Register the CustomUser model with the custom UserAdmin
admin.site.register(CustomUser, CustomUserAdmin)

