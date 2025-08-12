from django.db import models
from crawler.models import Crawler
from domain.models import Domain
from gatekeeper.models.company_info import Company  # Adjust the import path as needed

class Agreement(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='agreements')
    allowed_domains = models.ManyToManyField(Domain, blank =True, null =True, related_name='allowed_domain')
    allowed_crawlers = models.ManyToManyField(Crawler, blank=True, null=True, related_name='allowed_crawler')
    authorization = models.BooleanField(default=True)
    description = models.JSONField(default=dict, null=True, blank=True)

    def __str__(self):
        return f"Agreement for {self.company}"
