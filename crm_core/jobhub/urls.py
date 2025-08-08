from django.urls import path
from .views.job import Job



app_name = 'jobhub'

urlpatterns = [
    path('createjob/',Job.as_view(), name='job'),
    
]