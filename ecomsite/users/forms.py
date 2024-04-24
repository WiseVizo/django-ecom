from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    shipping_address = forms.CharField(widget=forms.Textarea)
    phone_number = forms.CharField(max_length=15)
    class meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'shipping_address', 'phone_number']