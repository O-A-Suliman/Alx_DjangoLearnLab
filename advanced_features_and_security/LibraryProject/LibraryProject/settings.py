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

# Redirect all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = True  # Forces HTTPS on all requests
# Tell Django how to detect HTTPS when behind a proxy (like Nginx)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Ensure cookies are only sent via HTTPS
SESSION_COOKIE_SECURE = True   # Secure session cookies
CSRF_COOKIE_SECURE = True      # Secure CSRF cookies

# Browser-side security protections
X_FRAME_OPTIONS = 'DENY'  # Prevent clickjacking
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent MIME-type sniffing
SECURE_BROWSER_XSS_FILTER = True  # Enable browser XSS filtering

# ==========================
# APPLICATION DEFINITION
# ==========================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',
    'csp',  # Content Security Policy (optional)
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',  # CSP middleware
]

ROOT_URLCONF = 'LibraryProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'LibraryProject.wsgi.application'

# ==========================
# DATABASE
# ==========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ==========================
# PASSWORD VALIDATION
# ==========================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ==========================
# INTERNATIONALIZATION
# ==========================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ==========================
# STATIC FILES
# ==========================
STATIC_URL = 'static/'

# ==========================
# DEFAULT PRIMARY KEY FIELD
# ==========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ==========================
# CUSTOM USER MODEL
# ==========================
AUTH_USER_MODEL = 'bookshelf.CustomUser'

# ==========================
# CONTENT SECURITY POLICY
# ==========================
CONTENT_SECURITY_POLICY = {
    "DIRECTIVES": {
        "default-src": ("'self'",),
        "style-src": ("'self'", "https://fonts.googleapis.com"),
        "font-src": ("'self'", "https://fonts.gstatic.com"),
        "script-src": ("'self'",),
    },
    "EXCLUDE_URL_PREFIXES": ("/admin",),
}
