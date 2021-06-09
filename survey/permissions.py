from rest_framework import permissions

class IsSuperUserOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
<<<<<<< HEAD
        return request.user.is_superuser
=======
        return request.user.is_superuser
>>>>>>> 17e482e7b18bc60b63f7d48788237b22c270d5e1
