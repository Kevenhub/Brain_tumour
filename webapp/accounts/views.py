# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm


def home_view(request):
    """Homepage after login"""
    return render(request, "accounts/home.html")

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")  # change this to your homepage name
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/register.html", {"form": form})

def login_view(request):
    """Handles user login"""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")

    return render(request, "accounts/login.html")


def logout_view(request):
    """Logs user out"""
    logout(request)
    return redirect("login")
