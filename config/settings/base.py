"""

Django settings for config project.



Generated by 'django-admin startproject' using Django 4.2.



For more information on this file, see

https://docs.djangoproject.com/en/4.2/topics/settings/



For the full list of settings and their values, see

https://docs.djangoproject.com/en/4.2/ref/settings/

"""



from pathlib import Path

import os

import django.middleware.locale
from django.utils.translation import gettext_lazy as _



# Build paths inside the project like this: BASE_DIR / 'subdir'.



# Quick-start development settings - unsuitable for production

# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/



# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = str(os.environ.get('SECRET_KEY'))



# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True



if os.environ.get('DB') == 'on':

    from .production import *

else:

    from .development import *


ALLOWED_HOSTS = ["*"]



# Application definition



INSTALLED_APPS = [

    'modeltranslation',



    'jazzmin',

    'django.contrib.admin',

    'django.contrib.auth',

    'django.contrib.contenttypes',

    'nested_admin',

    'django.contrib.sessions',

    'django.contrib.messages',

    'django.contrib.staticfiles',

    'ckeditor',

    'ckeditor_uploader',

    'django_ckeditor_5',



    # docs

    'drf_yasg',



    # rest

    'rest_framework',



    # apps

    'apps.main_page',

    'apps.data',

]

MODELTRANSLATION_CUSTOM_FIELDS = ('CKEditor5Field', )


MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',

    'corsheaders.middleware.CorsMiddleware',
    
    'django.middleware.common.CommonMiddleware',

    'django.middleware.locale.LocaleMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]



ROOT_URLCONF = 'config.urls'



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



WSGI_APPLICATION = 'config.wsgi.application'



REST_FRAMEWORK = {

    'DEFAULT_PERMISSION_CLASSES': [

        'rest_framework.permissions.AllowAny',

    ],

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',

    'PAGE_SIZE': 8,



    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',

}



# Database

# https://docs.djangoproject.com/en/4.2/ref/settings/#databases



DATABASES = DATABASES



# Password validation

# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators



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



# Ckeditor
customColorPalette = [
    {
        'color': 'hsl(4, 90%, 58%)',
        'label': 'Red'
    },
    {
        'color': 'hsl(340, 82%, 52%)',
        'label': 'Pink'
    },
    {
        'color': 'hsl(291, 64%, 42%)',
        'label': 'Purple'
    },
    {
        'color': 'hsl(262, 52%, 47%)',
        'label': 'Deep Purple'
    },
    {
        'color': 'hsl(231, 48%, 48%)',
        'label': 'Indigo'
    },
    {
        'color': 'hsl(207, 90%, 54%)',
        'label': 'Blue'
    },
]

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': [
            'heading', '|', 'bold', 'italic', 'link',
            'bulletedList', 'numberedList', 'blockQuote', 'imageUpload', 'mediaEmbed'
        ],
        'mediaEmbed': {
            'previewsInData': True
        }
    },
    'extends': {
        'blockToolbar': [
            'paragraph', 'heading1', 'heading2', 'heading3',
            '|',
            'bulletedList', 'numberedList',
            '|',
            'blockQuote',
        ],
        'toolbar': [
            'heading', '|', 'outdent', 'indent', '|', 'bold', 'italic', 'link', 'underline', 'strikethrough',
            'code', 'subscript', 'superscript', 'highlight', '|', 'codeBlock', 'sourceEditing', 'insertImage',
            'bulletedList', 'numberedList', 'todoList', '|', 'blockQuote', 'imageUpload', '|',
            'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', 'mediaEmbed', 'removeFormat',
            'insertTable',
        ],
        'image': {
            'toolbar': ['imageTextAlternative', '|', 'imageStyle:alignLeft',
                        'imageStyle:alignRight', 'imageStyle:alignCenter', 'imageStyle:side', '|'],
            'styles': [
                'full',
                'side',
                'alignLeft',
                'alignRight',
                'alignCenter',
            ]
        },
        'table': {
            'contentToolbar': ['tableColumn', 'tableRow', 'mergeTableCells',
                               'tableProperties', 'tableCellProperties'],
            'tableProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            },
            'tableCellProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            }
        },
        'heading': {
            'options': [
                {'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph'},
                {'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1'},
                {'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2'},
                {'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3'}
            ]
        }
    },
    'list': {
        'properties': {
            'styles': 'true',
            'startIndex': 'true',
            'reversed': 'true',
        }
    }
}


CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'



# Internationalization

# https://docs.djangoproject.com/en/4.2/topics/i18n/



LANGUAGES = (

    ('ky', _('Kyrgyz')),

    ('ru', _('Russian')),

    ('en', _('English')),

) 






LANGUAGE_CODE = 'ru'



TIME_ZONE = 'UTC'



USE_I18N = True


LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]



USE_TZ = True



# Static files (CSS, JavaScript, Images)

# https://docs.djangoproject.com/en/4.2/howto/static-files/



STATIC_URL = "/back_static/"

STATIC_ROOT = os.path.join(BASE_DIR, "back_static")

STATICFILE_DIRS = [
    os.path.join(BASE_DIR, 'local_static')
]



MEDIA_URL = '/back_media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "back_media")





CKEDITOR_UPLOAD_PATH = "uploads/"



# Default primary key field type

# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'





SPECTACULAR_SETTINGS = {

    'TITLE': 'NCOMID API',

    'DESCRIPTION': 'NCOMID description',

    'VERSION': '1.0.0',

    'SERVE_INCLUDE_SCHEMA': False,

}



# CSRF_TRUSTED_ORIGINS = ['*']



CORS_ALLOW_ALL_ORIGINS = True


DATA_UPLOAD_MAX_MEMORY_SIZE = 20000000

CSRF_TRUSTED_ORIGINS = [
    'https://lotos-cleaning.pp.ua',
    'http://51.20.108.79:80/',
    'http://localhost:8000'
]

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')