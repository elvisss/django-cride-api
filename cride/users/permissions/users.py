"""User permission classes"""

from rest_framework.permissions import BasePermission

# from cride.users.models import User

class IsAccountOwner(BasePermission):
    """Allow access only to objects owned by the requesting user."""
    def has_object_permission(self, request, view, obj):
        """Check obj and user are the same."""
        return request.user == obj
