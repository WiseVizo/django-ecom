from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Welcome {username} u have successfully registered!")
            print(f"logged in as {username}")
            return redirect("users:login")
    else:
        form = RegistrationForm()
    
    return render(request, "users/register.html", {'form': form,})


def logout_form(request):
    return render(request, "users/logout_form.html")