from django.views import View
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from ..models.user import User

@method_decorator(login_required, name='dispatch')
class DeleteOpsUser(View):
    def post(self, request, user_id):
        user = get_object_or_404(User, id=user_id, client_id=request.user.client_id, user_type='client_ops')
        user.delete()
        return redirect('gatekeeper:ListAllOpsUser')