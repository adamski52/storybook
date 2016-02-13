from rest_framework import permissions

class IsNotAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_authenticated()

    def has_object_permissions(self, request, view, obj):
        return not request.user.is_authenticated()

class OneToOneCreate(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == "destroy":
            return request.user.is_staff

        if view.action == "create" or view.action == "list":
            if request.user.is_authenticated():
                if request.user.is_staff:
                    return True
                return request.user.family is None
            return False

        if view.action == "update" or view.action == "partial_update":
            return request.user.is_authenticated()

        return True
 
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj == request.user



class OneTimeCreate(permissions.BasePermission):
    def has_permission(self, request, view):        
        if view.action == "destroy":
            return request.user.is_staff

        if view.action == "create" or view.action == "list":
            if request.user.is_authenticated():
                return request.user.is_staff
            return True

        if view.action == "update" or view.action == "partial_update":
            return request.user.is_authenticated()

        return True
 
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj == request.user