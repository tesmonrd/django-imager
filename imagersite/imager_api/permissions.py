from rest_framework import permissions


class ApiPermissions(permissions.BasePermission):
    """Establish permissions."""

    def has_permission(self, request, view, obj):
        """Define permission."""
        if request.method != 'GET':
            return False
        return obj.owner == request.user
