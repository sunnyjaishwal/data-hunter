
import os   
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm_core.settings')
django.setup()





from crawler.models import Crawler
import redis


site_names_cache = redis.Redis(host='localhost', port=6379, db=1)

SITE_NAMES_CACHE_KEY = "all_crawler_names"

def refresh_site_names_cache():
    site_names = list(Crawler.objects.values_list('crawler_name', flat=True))
    site_names_cache.set(SITE_NAMES_CACHE_KEY, "||".join(site_names))  # Store as joined string or use other serialize method
    return site_names

def get_cached_site_names():
    cached = site_names_cache.get(SITE_NAMES_CACHE_KEY)
    if cached:
        return cached.decode("utf-8").split("||")
    else:
        return refresh_site_names_cache()
    
print("Cached site names:", get_cached_site_names())
