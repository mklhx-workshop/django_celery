from __future__ import absolute_import

import os

from celery import Celery

# from django_celery.settings import CELERY_BROKER_URL

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_celery.settings")

app = Celery("django_celery")
#     ,
#     broker=CELERY_BROKER_URL,
#     include=["django_celery.tasks"],
# )

# Optional configuration, see the application user guide.
# app.conf.update(
#     result_expires=3600,
# )

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")


# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# if __name__ == "__main__":
#     app.start()
