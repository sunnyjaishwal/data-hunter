from django.contrib import admin
from .models import Job
from .models import JobType
from .models import ClientJobPermission

@admin.register(JobType)
class JobTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'job_type', 'status', 'created_at')
    list_filter = ('status', 'job_type')
    search_fields = ('title', 'client__email')
    autocomplete_fields = ('client', 'job_type')



@admin.register(ClientJobPermission)
class ClientJobPermissionAdmin(admin.ModelAdmin):
    list_display = ('client', 'allowed_job_type')
    list_filter = ('allowed_job_type',)
    search_fields = ('client__email',)
    autocomplete_fields = ('client', 'allowed_job_type')

    def get_queryset(self, request):
        # Optional: only show clients in the dropdown
        qs = super().get_queryset(request)
        return qs.select_related('client', 'allowed_job_type')
