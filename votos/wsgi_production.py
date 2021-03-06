import os
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "votos.settings.production")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
