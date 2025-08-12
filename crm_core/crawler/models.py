from django.db import models
from domain.models import Domain  # Import Domain from domain app

class Crawler(models.Model):
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, related_name='crawlers')
    crawler_name = models.CharField(max_length=255)

    def __str__(self):
        return self.crawler_name
