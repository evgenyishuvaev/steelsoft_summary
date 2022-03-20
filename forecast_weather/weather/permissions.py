from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    '''If user is owner or staff, then he has access
    '''
    
    def has_permission(self, request, view):

        print(request.method)

        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.is_anonymous:
            return False

        return request.user.is_forecaster or request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return (obj.owner == request.user) or request.user.is_staff


class IsForecasterOrAdminElseReadOnly(permissions.BasePermission):
    '''If user is forecaster or staff, then he has access to Create, else only to List
    '''

    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.is_anonymous:
            return False

        return bool(request.user.is_forecaster or request.user.is_staff)

    def has_object_permission(self, request, view, obj):
        return bool(request.user.is_forecaster or request.user.is_staff)