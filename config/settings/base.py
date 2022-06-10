"""
Django settings for insurancePersonalizationAndRecommendation project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
from django.utils.translation import ugettext_lazy as _
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_ROOT =  Path(__file__).resolve().parent.parent.parent/'static'

DATA_FILE_DIR = Path(__file__).resolve().parent.parent.parent/'data'

GRAPPELLI_ADMIN_TITLE ='Insurance Personalization and Recommendations'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z_l0dnkacydps)ust146uysxr#3i3&8j)u%y$(ma7^w7=&+7v*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


ALLOWED_HOSTS = ['*',]
ALLOWED_GROUPS = {
    'maker' : 'CIBCADMIN',
    'checker':  'CIBCSUPERVISOR'
}
WORKFLOW_OBJECTS = ['Objection']

AVATARS_SERVER_URL = 'http://127.0.0.1:3000'

# Application definition

INSTALLED_APPS = [
    'insurancePersonalizationAndRecommendation.accounts',
    'insurancePersonalizationAndRecommendation.insuranceProducts',
    'insurancePersonalizationAndRecommendation.stories',
    'grappelli',
    'bootstrap5',
    "crispy_forms",
    "crispy_bootstrap5",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_yasg',
    'rest_framework.authtoken',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'django.contrib.sites',
    'django_extensions',
    'django_auth_adfs',
    "debug_toolbar",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

if os.environ.get('SQL_DEBUG', False):
    MIDDLEWARE += ('sql_middleware.SqlPrintingMiddleware',)

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.parent.joinpath('insurancePersonalizationAndRecommendation').joinpath('templates'))],
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

WSGI_APPLICATION = 'config.wsgi.application'

LOGOUT_REDIRECT_URL = '/auth/login/'
# Configure django to redirect users to the right URL for login
LOGIN_URL = "/auth/login/"
# LOGIN_URL = "django_auth_adfs:login"
# LOGIN_REDIRECT_URL = "/insurance/ci_pre_application"
LOGIN_REDIRECT_URL = "/account/home/"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_USER_MODEL = 'accounts.CustomUser'
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGES = (
    ('en', _('English')),
    ('fr', _('French')),
    ('en-us', _('English US')),
    ('en-ca', _('English Canada')),
    ('fr-ca', _('French Canada')),
)

LANGUAGE_CODE = 'en-us'

LOCALE_PATHS = (
    BASE_DIR / 'locale',
)

DEFAULT_ERROR_MESSAGE = _("An error has occurred")

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR.parent.joinpath('insurancePersonalizationAndRecommendation').joinpath('static'),
]


CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

# Default settings
BOOTSTRAP5 = {

    # The complete URL to the Bootstrap CSS file
    # Note that a URL can be either a string,
    # e.g. "https://stackpath.bootstrapcdn.com/bootstrap/5.1.1/css/bootstrap.min.css",
    # or a dict like the default value below.
    "css_url": {
        "href": "https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css",
        "integrity": "sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB",
        "crossorigin": "anonymous",
    },

    # The complete URL to the Bootstrap JavaScript file
    "javascript_url": {
        "url": "https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js",
        "integrity": "sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T",
        "crossorigin": "anonymous",
    },

    # The complete URL to the Bootstrap CSS file (None means no theme)
    "theme_url": None,

    # Put JavaScript in the HEAD section of the HTML document (only relevant if you use bootstrap5.html)
    'javascript_in_head': False,

    # Label class to use in horizontal forms
    'horizontal_label_class': 'col-md-3',

    # Field class to use in horizontal forms
    'horizontal_field_class': 'col-md-9',

    # Set placeholder attributes to label if no placeholder is provided
    'set_placeholder': True,

    # Class to indicate required (better to set this in your Django form)
    'required_css_class': '',

    # Class to indicate error (better to set this in your Django form)
    'error_css_class': 'is-invalid',

    # Class to indicate success, meaning the field has valid input (better to set this in your Django form)
    'success_css_class': 'is-valid',

    # Renderers (only set these if you have studied the source and understand the inner workings)
    'formset_renderers':{
        'default': 'bootstrap5.renderers.FormsetRenderer',
    },
    'form_renderers': {
        'default': 'bootstrap5.renderers.FormRenderer',
    },
    'field_renderers': {
        'default': 'bootstrap5.renderers.FieldRenderer',
        'inline': 'bootstrap5.renderers.InlineFieldRenderer',
    },
}


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'django_auth_adfs.backend.AdfsAuthCodeBackend',
]

SITE_ID = 2

# Additional configuration settings
SOCIALACCOUNT_QUERY_EMAIL = True
ACCOUNT_LOGOUT_ON_GET= True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'none'


# checkout the documentation for more settings
client_id = '29cb4877-bb9a-4c37-877b-20f5f148c4bd'
client_secret = 'XK18Q~roOHDX96q24sgiqaS1YeSC0ljxG7PmlcgB'
tenant_id = '7443f4e9-c7e3-4938-8119-7658730978a5'


AUTH_ADFS = {
    'AUDIENCE': client_id,
    'CLIENT_ID': client_id,
    'CLIENT_SECRET': client_secret,
    'CLAIM_MAPPING': {'first_name': 'given_name',
                      'last_name': 'family_name',
                      'email': 'upn'},
    'GROUPS_CLAIM': 'go1',
    'MIRROR_GROUPS': True,
    'USERNAME_CLAIM': 'upn',
    'TENANT_ID': tenant_id,
    'RELYING_PARTY_ID': client_id,
}

CUSTOM_FAILED_RESPONSE_VIEW = 'dot.path.to.custom.views.login_failed'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'sql.log',
        },
    },
    'loggers': {
        'django.db.backends': {
            'sql_middleware': {
                'handlers': ['file'],
                'level': 'DEBUG',
                'propagate': True,
            },
        },
    },
}

INTERNAL_IPS = [
    "127.0.0.1",
]