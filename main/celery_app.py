# # celery.py
# from __future__ import absolute_import, unicode_literals
# import os
# from celery import Celery
# from time import sleep
#
# import dotenv
# dotenv.load_dotenv()
# # from file_app.tasks import MyTask
#
# # Set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
#
# # Create a Celery instance and configure it with the Django settings.
# celery_app = Celery('main')
#
# # Load task modules from all registered Django app configs.
# celery_app.config_from_object('django.conf:settings', namespace='CELERY')
#
# celery_app.conf.update(
#     accept_content=['json','pickle'],
#     task_serializer='pickle',
# )
#
# # Auto-discover tasks in all installed apps.
# celery_app.autodiscover_tasks()
#
# # celery_app.register_task(MyTask)
#
