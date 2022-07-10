from rest_framework import permissions


class AdUpdatePermission(permissions.BasePermission):
    message = 'Update ads for non owner user or admin/moderator not allowed.'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author:
            return True
        elif request.user.role == 'admin' or request.user.role == 'moderator':
            return True
        return False


class AdDeletePermission(permissions.BasePermission):
    message = 'Delete ads for non owner user or admin/moderator not allowed.'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author:
            return True
        elif request.user.role == 'admin' or request.user.role == 'moderator':
            return True
        return False
