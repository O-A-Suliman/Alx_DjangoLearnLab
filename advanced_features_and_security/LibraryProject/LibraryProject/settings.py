"""
Django settings for LibraryProject project.

Enhanced for HTTPS security configuration.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ==========================
# SECURITY SETTINGS
# ==========================

SECRET_KEY = 'django-insecure-aawfkgj@h1xo$4(e#a=s&mryfksnezij%pp9#-5m8-zc7eke!='

# ❗ Disable debug in production
DEBUG = False

# Allow only production domain + localhost for testing
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.yourdomain.com']

# ==========================
# HTTPS & SECURITY ENFORCEMENT
# ==========================

# Redirect all HTTP requests

