"""Base settings to build other settings files upon."""

import environ
import os
from .constants import *

ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR_2 = ROOT_DIR.path('taximil/apps')
APPS_DIR = ROOT_DIR.path('taximil')

root = environ.Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
env = environ.Env(DEBUG=(bool, False), )
environ.Env.read_env()

# Base
DEBUG = env.bool('DJANGO_DEBUG', False)

# Language and timezone
TIME_ZONE = 'America/Mexico_City'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

# DATABASES

DATABASES = {
    'default': env.db()
}

DATABASES['default']['ATOMIC_REQUESTS'] = True

# URLs
ROOT_URLCONF = 'config.urls'

# WSGI
WSGI_APPLICATION = 'config.wsgi.application'

# ASGI
# ASGI_APPLICATION = 'config.settings.routing.application'

# USERS AND AUTHENTICATION
AUTH_USER_MODEL = 'users.User'

# Apps
DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.gis',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'swagger_ui',
    'corsheaders',
    'rest_framework_gis'
]
LOCAL_APPS = [
    'taximil.apps.users.apps.UsersAppConfig',
    'taximil.apps.common.apps.CommonsAppConfig'
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# Passwords
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    }
]

# Middlewares
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# # Static files
# STATIC_ROOT = str(ROOT_DIR('static'))
# STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     str(APPS_DIR.path('static')),
# ]
# STATICFILES_FINDERS = [
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# ]
#
# # Media
# MEDIA_ROOT = str(APPS_DIR('media'))
# MEDIA_URL = '/media/'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(APPS_DIR.path('templates')),
        ],
        'OPTIONS': {
            'debug': DEBUG,
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Security
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

# Email
# EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')

# Admin
ADMIN_URL = 'admin/'
ADMINS = [
    ("""Misael Gonzalez""", 'misael@gmail.com'),
]
MANAGERS = ADMINS

# Celery
# INSTALLED_APPS += ['taximil.apps.taskapp.celery.CeleryAppConfig']
# if USE_TZ:
#     CELERY_TIMEZONE = TIME_ZONE
# CELERY_BROKER_URL = env('CELERY_BROKER_URL')
# CELERY_RESULT_BACKEND = CELERY_BROKER_URL
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TASK_TIME_LIMIT = 5 * 60
# CELERY_TASK_SOFT_TIME_LIMIT = 60
#
# redis_host = os.environ.get('REDIS_HOST', '127.0.0.1')

# Channel layer definitions
# http://channels.readthedocs.io/en/latest/topics/channel_layers.html
# CHANNEL_LAYERS = {
#     "default": {
#         # This example app uses the Redis channel layer implementation channels_redis
#         "BACKEND": "channels_redis.core.RedisChannelLayer",
#         "CONFIG": {
#             "hosts": [(redis_host, 6379)],
#         },
#     },
# }

# Django rest framework
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    # Parser classes priority-wise for Swagger
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.JSONParser',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'EXCEPTION_HANDLER': 'taximil.utils.custom_handler_error.custom_exception_handler',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 30
}


STATICFILES_DIRS = [
     str(APPS_DIR.path('static')),
]
STATIC_ROOT = str(ROOT_DIR('static'))
STATIC_URL = '/static/'

# Media
MEDIA_ROOT = str(APPS_DIR('media'))
MEDIA_URL = '/media/'

UPLOAD_ROOT = 'media/uploads/'

DOWNLOAD_ROOT = os.path.join(ROOT_DIR, "static/media/downloads")
DOWNLOAD_URL = STATIC_URL + "media/downloads"

