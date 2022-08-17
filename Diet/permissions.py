from rest_framework.permissions import BasePermission ,SAFE_METHODS
class custompermissions(BasePermission):
    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        if request.method in SAFE_METHODS :
            print(request.user)
            return True
        else:
            pass

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return True