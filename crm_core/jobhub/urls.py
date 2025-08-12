from django.urls import path
from .views.job import Job
from .views.list_all_jobs import ListAllJobs
from .views.update_job import UpdateJob
from .views.delete_jobs import DeleteJobs


app_name = 'jobhub'

urlpatterns = [
    path('createjob/',Job.as_view(), name='job'),
    path('listalljobs/', ListAllJobs.as_view(), name='ListAllJobs'),
    path('updatejob/<int:pk>/', UpdateJob.as_view(), name='UpdateJob'),
    path('deletejob', DeleteJobs.as_view(), name="DeleteJobs")
]