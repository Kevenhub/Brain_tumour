from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import CustomLogoutView

urlpatterns = [
    path("", views.landing,name="landing"),
    path("home/", views.home, name="home"),
    path("register/", views.register, name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login"
    ),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]