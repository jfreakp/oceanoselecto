"""
WSGI config for Vercel deployment.

Exposes a module-level variable named ``app`` required by Vercel's Python runtime.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oceanoselecto.settings")

# Vercel expects a variable named `app` for WSGI
app = get_wsgi_application()
