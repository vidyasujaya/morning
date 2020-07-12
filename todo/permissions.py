from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        #All permissions only allowed to object owners
        #obj.user == obj.owner
        return obj.user == request.user