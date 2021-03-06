#coding=utf-8
"""
Django settings for messages project.

Generated by 'django-admin startproject' using Django 1.9.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
# import ldap
import logging
# from django_auth_ldap.config import LDAPSearch, ActiveDirectoryGroupType
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q#sb(r=52zwc)*n(kbe74a6xjr@-gc#ukieb+d3u8s1+y9(f0b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['10.99.69.35','10.99.69.36','ips.eju-inc.com']


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
    'django_extensions',
    'api',
    'django_select2',
    'webui',
    'bootstrap_pagination',
    'corsheaders',
    'djcelery',
]

MIDDLEWARE_CLASSES = [
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # "django.core.context_processors.six",
]

ROOT_URLCONF = 'ips.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'ips.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db1.sqlite3'),
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ips',
        'USER': 'ipsadmin',
        'PASSWORD': 'Eju@ips1',
        'HOST': '10.99.69.35',
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'core.pagination.DefaultResultsSetPagination',
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework_filters.backends.DjangoFilterBackend',
    ),
}


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    'c:\\work\\open\\ips\\static',
    # '/opt/app/ips/static',
)
import djcelery
from kombu import Exchange, Queue
djcelery.setup_loader()
# Celery Settings
BROKER_URL = 'redis://:cc62601845fc3c66cdbb81915a871605@10.99.69.35:6379/3'
CELERY_RESULT_BACKEND = 'redis://:cc62601845fc3c66cdbb81915a871605@10.99.69.35:6379/2'
# CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
CELERY_QUEUES = (
    Queue('10.99.70.27'),
    Queue('10.99.70.33'),
    # Queue('for_task_B', Exchange('for_task_B'), routing_key='for_task_B'),
)


CORS_ORIGIN_ALLOW_ALL = True

# LOG_PATH = '/opt/app/ips/act.log'
LOG_PATH = 'c:\\work\\open\\ips\\act.log'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '[%(asctime)s] %(levelname)s %(module)s.%(funcName)s-[%(lineno)d] %(message)s'
        },
    },
    'filters': {
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'standard',
        },
        'windows_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_PATH,
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'windows_handler'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django': {
            'handlers': ['windows_handler'],
            'level': 'INFO',
            'propagate': False
        },
        'webapp': {
            'handlers': ['windows_handler'],
            'level': 'INFO',
            'propagate': False
        },
        'ips': {
            'handlers': ['windows_handler'],
            'level': 'DEBUG',
            'propagate': False
        }
    }
}

# Debug Toolbar
# DEBUG_TOOLBAR_CONFIG = {
#     'JQUERY_URL': '//apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js',
# }

LOGIN_REDIRECT_URL='/'
LOGIN_URL='/login/'
LOGOUT_REDIRECT_URL='/login/'





AUTH_LDAP_SERVER_URI = "ldap://172.28.100.101:389"
AUTH_LDAP_BIND_DN = unicode("CN=admin_cy,OU=创研中心,DC=shfang,DC=net","utf8")
AUTH_LDAP_BIND_PASSWORD = "Ehouse027="
OU=unicode('OU=创研中心,DC=shfang,DC=net', 'utf8')
AUTH_LDAP_USER_SEARCH = LDAPSearch(OU, ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)")

AUTH_LDAP_USER_ATTR_MAP = {
       "first_name": "givenName",
       "last_name": "sn",
       "email":"mail"
}

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)


# Select 2
AUTO_RENDER_SELECT2_STATICS = True
SELECT2_BOOTSTRAP = True
# Set the cache backend to select2
SELECT2_CACHE_BACKEND = 'select2'
REDIS_TIMEOUT=7*24*60*60
CUBES_REDIS_TIMEOUT=60*60
NEVER_REDIS_TIMEOUT=365*24*60*60
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://:cc62601845fc3c66cdbb81915a871605@10.99.69.35:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    'select2': {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://:cc62601845fc3c66cdbb81915a871605@10.99.69.35:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}