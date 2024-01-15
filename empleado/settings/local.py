from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado',
        'USER': 'postgres',
        'PASSWORD': 'devtest',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR /'static'] #se agrega para poder usar archvis estaticos como css immg

MEDIA_URL = '/media/' #median que quiero que se genere
MEDIA_ROOT = BASE_DIR /'media' #cual va ser la carpeta base donde se van a almacenar que busque la carpeta media


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
