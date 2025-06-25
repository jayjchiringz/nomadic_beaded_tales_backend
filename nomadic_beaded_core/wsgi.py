import os
from django.core.wsgi import get_wsgi_application

from whitenoise import WhiteNoise
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nomadic_beaded_core.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root=settings.MEDIA_ROOT, prefix='media/')
