from celery import shared_task
from .models.request import Request

@shared_task
def process_live_request(req_id):
    print(f"Processing request with ID: {req_id}")
    req= Request.objects.get(request_id=req_id)
    payload = req.parameter
    print(type(payload))
    print(payload, "will process crawler api with this payload")

def send_live_request_to_queue(request_id, crawler):
    print("will now prepare and send meassage to queue ")
    process_live_request.apply_async(
        args=(request_id,),
        queue=crawler,          # e.g. "airfrance", "marriot"
        routing_key=crawler
    )
