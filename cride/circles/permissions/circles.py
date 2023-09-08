"""Circle permission classes"""

from rest_framework.permissions import BasePermission

from cride.circles.models import Membership

class isCircleAdmin(BasePermission):
    """Allow access only to circle admins."""

    def has_object_permission(self, request, view, obj):
        """Verify user have a membership in the obj and is an admin."""
        try:
            Membership.objects.get(
                user=request.user,
                circle=obj,
                is_admin=True,
                is_active=True
            )
        except Membership.DoesNotExist:
            return False
        return True
