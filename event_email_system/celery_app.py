from __future__ import absolute_import, unicode_literals

import os

from django.conf import settings

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_email_system.settings')

app = Celery('event_email_system', broker=settings.BROKER_URL)
app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print("Hello from celery")

from celery.schedules import crontab
from datetime import timedelta

app.conf.beat_schedule = {
    'my_periodic_task': {
        'task': 'event_api.email_processing.send_emails_for_today_events',
        'schedule': crontab(hour=6, minute=0),  # Schedule at 6 am daily
        'schedule': timedelta(seconds=10), # run every 10 seconds
    },
}
