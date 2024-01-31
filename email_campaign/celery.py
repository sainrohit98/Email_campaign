import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

# celery.py (or tasks.py if you haven't separated it)
from celery import Celery
from celery.schedules import crontab

app = Celery('email_campaign')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_daily_campaigns': {
        'task': 'email_campaign.tasks.send_daily_campaigns',
        'schedule': crontab(minute=1),  # Adjust the time as needed
    },
}

