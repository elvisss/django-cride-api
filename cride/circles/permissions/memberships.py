"""Membership permission classes"""

from rest_framework.permissions import BasePermission

from cride.circles.models import Membership


class IsActiveCircleMember(BasePermission):
    """Allow access only to circle members."""

    def has_object_permission(self, request, view, obj):
        """Verify user is an active member of the circle."""
        try:
            Membership.objects.get(
                user=request.user,
                circle=view.circle,
                is_active=True
            )
        except Membership.DoesNotExist:
            return False

        return True

class IsSelfMember(BasePermission):
    """Allow access only to member owners."""

    def has_permission(self, request, view):
        """Let object permission grant access."""
        obj = view.get_object()
        return self.has_object_permission(request, view, obj)

    def has_object_permission(self, request, view, obj):
        """Allow access only to member owners."""
        return obj.user == request.user
