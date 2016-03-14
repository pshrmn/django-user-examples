import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "c_email_as_username.settings")

application = get_wsgi_application()
