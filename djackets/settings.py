"""
Django settings for djackets project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!x_9%**0--68m-os6jw%mb4s!+8ayg(p*+_*va*k%-!z85so5@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS=['*']

CORS_ORIGIN_ALLOW_ALL = False

CORS_ALLOWED_ORIGINS = [
    'https://vue-clothes.df.r.appspot.com',
    'http://localhost:8080'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
   
    
'rest_framework',
'rest_framework.authtoken',
'djoser',
'corsheaders',

'product',
'order',

'debug_toolbar',
]

MIDDLEWARE = [
'debug_toolbar.middleware.DebugToolbarMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',


]

ROOT_URLCONF = 'djackets.urls'

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

WSGI_APPLICATION = 'djackets.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

# # Database
# # https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# # Install PyMySQL as mysqlclient/MySQLdb to use Django's mysqlclient adapter
# # See https://docs.djangoproject.com/en/2.1/ref/databases/#mysql-db-api-drivers
# # for more information
# import pymysql  # noqa: 402
# pymysql.version_info = (1, 4, 6, 'final', 0)  # change mysqlclient version
# pymysql.install_as_MySQLdb()

# # [START db_setup]
# if os.getenv('GAE_APPLICATION', None):
#     # Running on production App Engine, so connect to Google Cloud SQL using
#     # the unix socket at /cloudsql/<your-cloudsql-connection string>
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.mysql',
#             'HOST': '/cloudsql/django-rest-clothes:asia-east1:mysql-clothes-second',
#             'USER': 'root',
#             'PASSWORD': 'winyake123',
#             'NAME': 'polls_mysql_clothes_second',
#         }
#     }
# else:
#     # Running locally so connect to either a local MySQL instance or connect to
#     # Cloud SQL via the proxy. To start the proxy via command line:
#     #
#     #     $ cloud_sql_proxy -instances=[INSTANCE_CONNECTION_NAME]=tcp:3306
#     #
#     # See https://cloud.google.com/sql/docs/mysql-connect-proxy
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.mysql',
#             'HOST': '127.0.0.1',
#             'PORT': '3306',
#             'NAME': 'polls_mysql_clothes_second',
#             'USER': 'root',
#             'PASSWORD': 'winyake123',
#         }
#     }
# # [END db_setup]

# # Use a in-memory sqlite3 database when testing in CI systems
# if os.getenv('TRAMPOLINE_CI', None):
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
#         }
#     }

# # Password validation
# # https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # noqa: 501
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # noqa: 501
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # noqa: 501
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # noqa: 501
#     },
# ]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT = 'static'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



#????????????django-debug-toolbar
INTERNAL_IPS=('127.0.0.1',)
