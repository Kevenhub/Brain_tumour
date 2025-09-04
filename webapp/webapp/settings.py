import os
import sys
from pathlib import Path

# BASE_DIR points to Brain_tumour_Final
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Add BASE_DIR to sys.path so Django can find "backend" (if needed)
sys.path.append(str(BASE_DIR))

SECRET_KEY = 'your-secret-key-here'
DEBUG = True
ALLOWED_HOSTS = []

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'tumor',
    'mlmodels',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'webapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # point only to "templates" folder
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'webapp.wsgi.application'

# Database (using sqlite3 for now)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ------------------------
# Static & Media Settings
# ------------------------

# URL prefix for static files
STATIC_URL = '/static/'

# Tell Django where your static files live (besides app-level static/)
STATICFILES_DIRS = [
    BASE_DIR / "webapp" / "static",   # ✅ correct location
]

# Where collectstatic will put all files
STATIC_ROOT = BASE_DIR / "staticfiles"

# Media files (uploaded files like MRI images)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "webapp" / "media"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = "upload"   # after login → go to upload page
LOGOUT_REDIRECT_URL = "home"
