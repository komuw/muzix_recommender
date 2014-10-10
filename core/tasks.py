from __future__ import absolute_import
from celery import shared_task, task
from django.conf import settings


# The @shared_task decorator lets you create tasks without having any concrete app instance:
@shared_task
def add(x, y):
    """
    You can import this example task as: from core.tasks import add
    """
    return x + y
