import os
from celery.schedules import crontab

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

app = Celery("makro_uz")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'delete-old-post-views-every-midnight': {
        'task': 'api.tasks.delete_old_post_views',
        'schedule': crontab(minute=1, hour=5),  # Запускать каждый день в полночь
    },
}
