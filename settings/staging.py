from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

# Add raven to the list of installed apps
INSTALLED_APPS = INSTALLED_APPS + (
    'debug_toolbar',
    'django_extensions',
)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'