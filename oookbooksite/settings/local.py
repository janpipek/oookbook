from .base import *

MIDDLEWARE_CLASSES += [
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

INSTALLED_APPS += [
    'debug_toolbar'
]

DEBUG = True

TEMPLATE_DEBUG = True

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS' : False,
}