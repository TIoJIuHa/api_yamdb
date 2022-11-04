from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.is_staff
            or request.user.is_superuser
            or request.user.role == "admin"
        )


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or (
            request.user.is_authenticated
            and (
                request.user.is_staff
                or request.user.is_superuser
                or request.user.role == "admin"
            )
        )


class IsAuthorModeratorAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return (
            request.method in SAFE_METHODS
            or obj.user == request.user
            or request.user.is_staff
            or request.user.is_superuser
            or request.user.role == "admin"
            or request.user.role == "moderator"
        )
