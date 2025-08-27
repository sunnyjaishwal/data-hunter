from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from gatekeeper.models.company_info import Company

class ClientAuthentication(BaseAuthentication):
   

    def authenticate(self, request):
        
        company = request.data.get('client_id')
        if not company:
            return None 
        try:
            customer = Company.objects.get(uuid=company)
        except customer.DoesNotExist:
            raise AuthenticationFailed('No customer with this uuid found.')

        return (customer, None)  
