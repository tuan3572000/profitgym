from .base import *

DEBUG = False


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'npk(^w4ccp&f0mey2z8$0fcd&ml$s6xngno_#d6_zr@dnk00x2'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

try:
    from .local import *
except ImportError:
    pass
