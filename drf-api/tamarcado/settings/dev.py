from tamarcado.settings.base import *

# overwrite from base
DEBUG = True
ALLOWED_HOSTS = []
LOGGING = {
    **LOGGING,
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console']
        }
    }
}