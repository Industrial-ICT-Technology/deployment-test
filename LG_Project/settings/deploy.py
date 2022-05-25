from .base import *
import django_heroku

DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

django_heroku.settings(locals())

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db0cqlppmpiuf',
        'USER': 'wdrcxaieibecgt',
        'PASSWORD': '8a5e7955e7fba0ac3d02acedce4b335e63603d4d95163b85bf7a4d341fefab38',
        'HOST': 'ec2-34-231-177-125.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}