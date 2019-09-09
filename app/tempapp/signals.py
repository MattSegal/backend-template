import logging

from django.db.models.signals import post_save
from django.dispatch import receiver
from django_q.tasks import async_task

from .models import User
from .tasks import do_nothing

logger = logging.getLogger(__name__)


@receiver(post_save, sender=User)
def save_user(sender, instance, **kwargs):
    user = instance
    async_task(do_nothing, str(user.pk))
