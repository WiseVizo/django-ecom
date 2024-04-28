from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser

class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'shipping_address', 'phone_number']