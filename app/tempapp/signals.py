import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User
from .tasks import do_nothing

logger = logging.getLogger(__name__)


@receiver(post_save, sender=User)
def save_user(sender, instance, **kwargs):
    user = instance
    do_nothing.delay(user.pk)
