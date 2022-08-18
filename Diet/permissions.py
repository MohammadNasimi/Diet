from rest_framework.permissions import BasePermission ,SAFE_METHODS
class custompermissions(BasePermission):
    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        if request.method in SAFE_METHODS and request.user:
            print(request.user)
            return True
        elif request.method  == 'POST' and request.user:
            print(request.user.kind_user)
            return True

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return True

class custompermissionsDiet_admin(BasePermission):
    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        if request.method in SAFE_METHODS and request.user:
            print(request.user)
            return True
        elif request.method  == 'POST' and request.user.kind_user == "1":
            return True

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return True