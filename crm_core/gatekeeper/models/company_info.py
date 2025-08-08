from django.db import models
import uuid


class Company(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    name = models.CharField(null=True, blank=True)
    limit = models.PositiveIntegerField(default = 10)
    created_on = models.DateField(auto_now=True)
    updated_on = models.DateField(auto_now_add = True)
    created_by = models.ForeignKey('gatekeeper.user', on_delete=models.SET_NULL, blank =True, null= True, related_name = "clientadmins_created")
    updated_by = models.ForeignKey('gatekeeper.user', on_delete=models.SET_NULL, blank = True, null=True, related_name= "clientadmins_updated")
    
    def __str__(self):
        return f"Client- { self.uuid} , limit- {self.limit} "
    