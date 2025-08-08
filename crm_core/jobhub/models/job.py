from django.db import models

# Create your models here.
class JobType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=255)
    client = models.ForeignKey('gatekeeper.User', on_delete=models.CASCADE, related_name='jobs')
    job_type = models.ForeignKey('JobType', on_delete=models.PROTECT)
    status = models.CharField(max_length=50, default='pending')
    website = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.job_type.name})"

# Only for 'client' users
class ClientJobPermission(models.Model):
    client = models.ForeignKey('gatekeeper.User', on_delete=models.CASCADE, limit_choices_to={'user_type': 'client_admin'})
    allowed_job_type = models.ForeignKey('JobType', on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('client', 'allowed_job_type')
