from rest_framework import permissions

class IsEmailVerified(permissions.BasePermission):
    message = {
        "status": 403,
        "mail_verified": False,
        "detail": "Email is not verified"
    }
    
    def has_permission(self, request, view):
        user = request.user
        
        if user.is_staff and user.merchant.email_verified:
            return True
        else:
            return False 

