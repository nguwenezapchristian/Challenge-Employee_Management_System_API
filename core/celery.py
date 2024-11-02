# core/celery.py
import os
from celery import Celery

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery('core')

# Load settings from Django's settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Base task to be inherited for error handling
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
