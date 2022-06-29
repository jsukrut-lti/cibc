from .base import *

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cibcdevdb',
        'HOST': 'cibc-dev-db.c8aqzm8dqrzg.ca-central-1.rds.amazonaws.com',
        'USER': 'postgres',
        'PASSWORD': '8mBUEdN0F13jStclgrpr',
        'PORT': '5432',
    }
}
