"""
WSGI config for danimiller project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os, sys

# add the virtualenv site-packages path to the sys.path
sys.path.append('<PATH_TO_VIRTUALENV>/Lib/site-packages')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "danimiller.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
