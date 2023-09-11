from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from django.conf import settings

class StaffPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


class HasAPIKey(permissions.BasePermission):
    def has_permission(self, request, view):
        key = request.headers.get('X-API-KEY', None)
        if key != settings.VOLV_API_KEY:
            raise PermissionDenied
        return True

