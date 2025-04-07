import os

from celery import Celery

#telling celery where to look for Django settings
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'football.settings')

app = Celery('football')


# app.config_from_object-simply telling celery to get it's settings from Django. Celery needs a way to differentiate Celery settings from
#Django settings by specifying namespace='CELERY' in the settings.py file
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# tells celery to search for tasks in all registered Django app configs
# Load task modules from all registered Django apps.
app.autodiscover_tasks()



# @app.task(bind=True, ignore_result=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')