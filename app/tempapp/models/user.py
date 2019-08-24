import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

USER_FIELDS = ["username", "email"]


class User(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)


def create_user(strategy, details, backend, user=None, *args, **kwargs):
    """Python social auth user creation override"""
    if user:
        return {"is_new": False}

    fields = dict(
        (name, kwargs.get(name, details.get(name)))
        for name in backend.setting("USER_FIELDS", USER_FIELDS)
    )
    if not fields:
        return

    is_new = True
    try:
        user = User.objects.get(email=fields["email"])
        is_new = False
    except User.DoesNotExist:
        user = strategy.create_user(**fields)

    return {"is_new": is_new, "user": user}
