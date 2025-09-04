from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm   # ✅ import your custom form
from django.contrib.auth.views import LogoutView


def landing(request):
    # This is shown to users who are NOT logged in
    if request.user.is_authenticated:
        return redirect("home")   # go to home if already logged in
    return render(request, "accounts/landing.html")

# Home Page (only for logged-in users)
@login_required(login_url="landing")
def home(request):
    return render(request, "accounts/home.html")


# Register View
def register(request):
    if request.user.is_authenticated:
        return redirect("home")   # 🚀 Prevent logged-in users from seeing register again

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)   # auto-login after registration
            messages.success(request, "Registration successful. Welcome!")
            return redirect("home")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/register.html", {"form": form})


# Login View
def user_login(request):
    if request.user.is_authenticated:
        return redirect("home")   # 🚀 Prevent logged-in users from seeing login again

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)