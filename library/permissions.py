from rest_framework import permissions


class CustomStudentPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        request_token = request.headers.get("Auth-Token")
        # TODO
        static_token = "Bearer "
        if request_token == static_token:
            return True
        return False


class CustomLibrarianPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        request_token = request.headers.get("Auth-Token")
        # TODO
        static_token = "Bearer "
        if request_token == static_token:
            return True
        return False