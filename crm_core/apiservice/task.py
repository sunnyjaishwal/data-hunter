from celery import shared_task
from .crawler_dispatcher import CRAWLER_FETCH_RESPONSE_MAP
from crm_core.redis.cache_processor import CrawlerRedisClient

redis_client= CrawlerRedisClient(0)

@shared_task
def process_live_request(request_data):
    print(f"Processing request from queue")
    crawler_name = request_data['site_name']
    parameter = request_data['parameter']
    domain_name = request_data['domain_name']
    hotel_id = parameter.get("hotel_id")
    check_in_date = parameter.get("check_in_date")
    check_out_date = parameter.get("check_out_date")
    guest_count = parameter.get("guest_count", 1)
    fetch_response_func = CRAWLER_FETCH_RESPONSE_MAP.get(crawler_name)
    if not fetch_response_func:
        response = {
            "status": "error",
            "message": f"No fetch_response mapped for crawler '{crawler_name}'"
        }
    else:
        try:
            response = fetch_response_func.get_search_data(hotel_id, check_in_date, check_out_date, int(guest_count))
        except Exception as e:
            print(e)
            response = "No Response from crawler"
    
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
