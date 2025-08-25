from celery import shared_task
from .models.request import Request
from .cache_processor import CrawlerRedisClient

@shared_task
def process_live_request(req_id):
    print(f"Processing request with ID: {req_id}")
    req= Request.objects.get(request_id=req_id)
    payload = req.parameter
    crawler_name= req.site_name
    domain_name= req.domain_name
    response = "Dummy Response"
    redis_client= CrawlerRedisClient()
    key = redis_client.build_key(crawler_name, payload, domain_name)
    redis_client.set_crawler_response(key, response)
    return response

def send_live_request_to_queue(request_id, crawler):
    print("will now prepare and send meassage to queue ")
    process_live_request.apply_async(
        args=(request_id,),
        queue=crawler,          # e.g. "airfrance", "marriot"
        routing_key=crawler
    )
