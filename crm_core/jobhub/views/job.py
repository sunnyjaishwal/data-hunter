from django.shortcuts import render
from django.views import View
from django.http.response import HttpResponse
# Create your views here.

class Job(View):

    def get(self, *agrs, **kwargs):
        return HttpResponse(
            content={
                'data':'get-job'
            }
        )

    def post(self, *args, **kwargs):
        return HttpResponse(
            content={
                'body':'post-job'
            }
        )