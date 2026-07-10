"""
Custom permission classes for HoLe The Spirits.
"""

from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAuthenticatedUser(BasePermission):
    """
    Allow access only to authenticated users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)


class IsAdmin(BasePermission):
    """
    Allow access only to Django Superusers.
    """

    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.is_superuser
        )


class IsManager(BasePermission):
    """
    Placeholder permission for Manager role.
    Will be connected to Staff module in future.
    """

    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and (
                request.user.is_superuser
                or request.user.is_staff
            )
        )


class IsStaff(BasePermission):
    """
    Placeholder permission for Staff role.
    """

    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
        )


class ReadOnly(BasePermission):
    """
    Allow read-only requests.
    """

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS