from django.urls import path
from .views.job import Job
from .views.home import Home


app_name = 'jobhub'

urlpatterns = [
    path('createjob/',Job.as_view(), name='job'),
    path('home/', Home.as_view(), name='home'),
]