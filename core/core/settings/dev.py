from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'ecomerce',
        'USER':'postgres',
        'PASSWORD':'1234',
        'HOST':'localhost'

    }
}