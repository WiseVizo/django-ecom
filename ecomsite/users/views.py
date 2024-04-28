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
            print(request.POST)  # Debug statement to print form data
            username = form.cleaned_data.get('username')
            messages.success(request, f"Welcome {username} u have successfully registered!")
            return redirect("users:login")
    else:
        form = RegistrationForm()
    
    return render(request, "users/register.html", {'form': form,})

@login_required
def logout_form(request):
    return render(request, "users/logout_form.html")