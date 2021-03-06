"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.11.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'blog/templates/blog')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
MEDIA_DIR = os.path.join(BASE_DIR, 'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ty*^)5u1++f823ykv&9q1p6c(fsri^g19#2yexu^$r_tt_d#oe'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sass_processor',
    'storages',
    'mdeditor',
    'blog',
    'blog.templatetags.markdown',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                'markdown': 'blog.templatetags.markdown',
            }
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mysite',
        'USER': 'admin',
        'PASSWORD': 'administrator',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

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

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'blog/static')
STATICFILES_DIRS = [
    STATIC_DIR,
]


SASS_PROCESSOR_ROOT = os.path.join(BASE_DIR, 'static')
SASS_PROCESSOR_INCLUDE_FILE_PATTERN = r'^.+\.(sass|scss)$'
SASS_PRECISION = 8
SASS_OUTPUT_STYLE = 'compressed'
SASS_TEMPLATE_EXTS = ['.html', '.haml']

LOGIN_REDIRECT_URL = '/'


# MEDIA
MEDIA_URL = '/media/'
MEDIA_ROOT = MEDIA_DIR


MDEDITOR_CONFIGS = {
    'default': {
        'language': 'en',
    }
}

# MDEDITOR_CONFIGS = {
#     'default': {
#         'width': '90% ',  # Custom edit box width
#         'heigth': 500,  # Custom edit box height
#         'toolbar': ["undo", "redo", "|",
#                     "bold", "del", "italic", "quote", "ucwords", "uppercase", "lowercase", "|",
#                     "h1", "h2", "h3", "h5", "h6", "|",
#                     "list-ul", "list-ol", "hr", "|",
#                     "link", "reference-link", "image", "code", "preformatted-text", "code-block", "table", "datetime"
#                                                                                                            "emoji",
#                     "html-entities", "pagebreak", "goto-line", "|",
#                     "help", "info",
#                     "||", "preview", "watch", "fullscreen"],  # custom edit box toolbar
#         'upload_image_formats': ["jpg", "jpeg", "gif", "png", "bmp", "webp"],  # image upload format type
#         'image_folder': 'editor',  # image save the folder name
#         'theme': 'default',  # edit box theme, dark / default
#         'preview_theme': 'default',  # Preview area theme, dark / default
#         'editor_theme': 'default',  # edit area theme, pastel-on-dark / default
#         'toolbar_autofixed': True,  # Whether the toolbar capitals
#         'search_replace': True,  # Whether to open the search for replacement
#         'emoji': True,  # whether to open the expression function
#         'tex': True,  # whether to open the tex chart function
#         'flow_chart': True,  # whether to open the flow chart function
#         'sequence': True,  # Whether to open the sequence diagram function
#         'watch': True,  # Live preview
#         'lineWrapping': False,  # lineWrapping
#         'lineNumbers': False  # lineNumbers
#     }
#
# }

try:
    from .local_settings import *
except ImportError:
    pass

if not DEBUG:
    import django_heroku

    django_heroku.settings(locals())
