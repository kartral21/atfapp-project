import logging
import os
from logging.handlers import RotatingFileHandler
from atfappproject.confighandler import *


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'orkg9kjr*vj2a+r-n7y+_%bch_5ad9a5rw-wv*f-+69-h770gg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'atfapp',
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

ROOT_URLCONF = 'atfappproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'atfappproject.wsgi.application'


# Database
# DATABASES = {
#     'default': {
#             'ENGINE': 'django.db.backends.postgresql_psycopg2',
#             'NAME': 'Ajax',
#             'USER': 'postgres',
#             'PASSWORD': 'postgres',
#             'HOST': '127.0.0.1',
#             'PORT': '5432',
#         }
# }
DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': POSTGRES_DB_NAME,
            'USER': POSTGRES_DB_USERNAME,
            'PASSWORD': POSTGRES_DB_PASSWORD,
            'HOST': POSTGRES_DB_HOST,
            'PORT': POSTGRES_DB_PORT,
        }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'


handlers = [RotatingFileHandler(filename=LOGGING_FILENAME, mode=LOGGING_MODE, maxBytes=int(LOGGING_MAXBYTES),
                                backupCount=int(LOGGING_BACKUPCOUNT))]
logging.basicConfig(handlers=handlers,
                    level=logging.DEBUG,
                    format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
                    datefmt='%d/%m/%Y%I:%M:%S %p')

logger = logging.getLogger(__name__)
logger.setLevel(LOGGING_LEVEL)