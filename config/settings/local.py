from .base import *

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cibc',
        'HOST': 'localhost',
        'USER': 'postgres',
        'PASSWORD': 'jayesh123',
        'PORT': '5432',
    }
}

# INSTALLED_APPS += ['debug_toolbar',]
