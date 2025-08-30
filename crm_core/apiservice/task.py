from celery import shared_task
from .models.request import Request
from .cache_processor import CrawlerRedisClient

@shared_task
def process_live_request(request_data):
    print(f"Processing request from queue")
    # req= Request.objects.get(request_id=req_id)
    crawler_name = request_data['site_name']
    parameter = request_data['parameter']
    domain_name = request_data['domain_name']
    response = {
        "status": "success",
        "data": {
            "message": f"Processed request for {crawler_name} with parameters {parameter}"
        }
    }
    redis_client= CrawlerRedisClient()
    key = redis_client.build_key(crawler_name, parameter, domain_name)
    redis_client.set_crawler_response(key, response)
    return response

def send_live_request_to_queue(request_data, crawler):
    print("will now prepare and send meassage to queue ")
    process_live_request.apply_async(
        args=(request_data,),
        queue=crawler,          # e.g. "airfrance", "marriot"
        routing_key=crawler
    )
