"""
Django settings for ecomelectronic project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, "static")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qw3_m9sx#^0u(0(e^38tp&drv4ymn)-2k+^$u588ta5&3-&hd@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'users',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'import_export',
]
# EMAIL_HOST = 'smtp.sendgrid.net'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'testsite_app'
# EMAIL_HOST_PASSWORD = 'mys3cr3tp4ssw0rd'
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = 'TestSite Team <noreply@example.com>'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# Indicates that we are using gmail
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'hetvispatel6@gmail.com'
EMAIL_HOST_PASSWORD = 'cpsyoajbtkrhmtiz'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecomelectronic.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR,],
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

WSGI_APPLICATION = 'ecomelectronic.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.mysql',
       'NAME': 'ecom', # make database in mysql and provide name here
       'USER': 'root',     # database user
       'PASSWORD': '',
       'HOST': '127.0.0.1',
       'PORT': '3306',     # see port number of sql in xamp panel
   }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': 'django_ex',
#         'HOST' : 'localhost',
#         'PORT' : 27017,
#         'USER' : 'rohan',
#         'PASSWORD' : '1234',
#         'AUTH_SOURCE': 'django_ex',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [STATIC_DIR, ]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'index'
LOGIN_URL = 'login'