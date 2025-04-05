from django.utils.deprecation import MiddlewareMixin
from .models import IpAddress
from accounts.session import UserInfoSession

class UserIPMiddleware(MiddlewareMixin):
    """
    Middleware to gather the user's IP address and store it in the request object.
    """
    
    def __init__(self, get_response):  
        self.get_response = get_response  

    def __call__(self, request):  
        # Get the user's IP address
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            # If there are multiple IPs, take the first one
            ip = x_forwarded_for.split(',')[0]
        else:
            # Fallback to REMOTE_ADDR
            ip = request.META.get('REMOTE_ADDR')
        

        response = self.get_response(request)  

        if not IpAddress.objects.filter(ip=ip).exists():
            IpAddress.objects.create(
                ip=ip
            )
            user_session = UserInfoSession(request)
            user_session.update_user_info({
                'ip_address': ip
            })
         
        
        return response  
        
