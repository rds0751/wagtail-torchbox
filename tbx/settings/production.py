from .base import *  # noqa

# Disable debug mode
DEBUG = False


# Facebook JSSDB app id
FB_APP_ID = '323944607389'

SECRET_KEY = 'CHANGEME!!!'


try:
    from .local import *  # noqa
except ImportError:
    pass
