from rest_framework import permissions


class UserPermissions(permissions.BasePermission):
    #Allows read-only access to anyone (even unauthenticated users in this case)
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
         
    #Requires the user to be authenticated AND, the object being accessed must be the user's own profile (obj == request.user)
        return bool(request.user.is_authenticated and obj==request.user)

    def has_permission(self, request, view):

        if view.basename in ['users']:
            #For anonymous/unauthenticated users
            if request.user.is_anonymous:
                return request.method in permissions.SAFE_METHODS
            return request.user.is_authenticated