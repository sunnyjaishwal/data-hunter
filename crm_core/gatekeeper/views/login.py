from django.views import View
from django.http.response import HttpResponse

class Login(View):

    def get(self, *args, **kwargs):
        return HttpResponse(
            content={
                'data':'get-Login'
            }
        )

    def post(self, *args, **kwargs):
        return HttpResponse(
            content={
                'data': 'post-Login'
            }
        )