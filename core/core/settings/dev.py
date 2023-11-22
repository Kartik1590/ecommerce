from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'ecomerce',
        'USER':'postgres',
        'PASSWORD':os.environ.get('PASSWORD'),
        'HOST':'localhost'

    }
}