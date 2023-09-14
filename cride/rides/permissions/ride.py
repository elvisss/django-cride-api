"""Rides permissions"""

from rest_framework.permissions import BasePermission

class IsRideOwner(BasePermission):
    """Verify requesting user is the ride owner."""

    def has_object_permission(self, request, view, obj):
        """Verify user is owner of the ride."""
        return request.user == obj.offered_by
