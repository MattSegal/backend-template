import logging

from rest_framework import permissions

logger = logging.getLogger(__name__)


class IsOwner(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object see it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        user = request.user
        owner = getattr(obj, 'owner', None)
        return user == owner
