from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """permission for Owner"""
    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        return False
