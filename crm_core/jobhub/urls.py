from django.urls import path
from .views.job import Job


urlpatterns = [
    path('',Job.as_view(), name='job')
]