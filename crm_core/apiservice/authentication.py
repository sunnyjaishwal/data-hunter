from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import get_user_model

User = get_user_model()

class ClientAuthentication(BaseAuthentication):
   

    def authenticate(self, request):
        
        email = request.data.get('client_id')
        if not email:
            return None 
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise AuthenticationFailed('No user with this email found.')

        return (user, None)  
