from .celery import app as celery_app

# This will make sure the app is always imported when  Django starts   
__all__ = ('celery_app',)