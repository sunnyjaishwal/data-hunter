import uuid
from django.db import models

class Request(models.Model):
    request_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    client_id = models.ForeignKey('gatekeeper.User', on_delete=models.CASCADE, related_name='request')
    domain_name = models.CharField(max_length=255)
    crawler_name = models.CharField(max_length=255)
    parameter = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return f"req_id- {str(self.request_id)}, crawler- {self.crawler_name}"
