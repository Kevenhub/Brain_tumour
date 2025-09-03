from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("accounts.urls")),         # ✅ homepage is accounts/home
    path("tumor/", include("tumor.urls")),
    path("accounts/", include("accounts.urls")),
]
