from rest_framework import permissions


class SelectionUpdatePermission(permissions.BasePermission):
    message = 'Update selections for non owner user or admin/moderator not allowed.'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        elif request.user.role == 'admin' or request.user.role == 'moderator':
            return True
        return False


class SelectionDeletePermission(permissions.BasePermission):
    message = 'Delete selections for non owner user or admin/moderator not allowed.'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        elif request.user.role == 'admin' or request.user.role == 'moderator':
            return True
        return False
