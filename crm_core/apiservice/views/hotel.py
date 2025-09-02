from rest_framework.views import APIView
from rest_framework.response import Response as apiResponse
from ..serializers.request import RequestSerializer
from ..celery_producer import send_live_request_to_queue
from ..throttling import CustomerRateThrottle
from crm_core.redis.cache_processor import CrawlerRedisClient
from time import sleep
redis_client = CrawlerRedisClient(0)

class Hotel(APIView):
    
    throttle_classes = [CustomerRateThrottle]
    
    def post(self, request):
        data = request.data.copy()
        data['domain_name'] = 'hotel'
        serializer = RequestSerializer(data=data)
        if serializer.is_valid():
            req = serializer.save()
            crawler_name = req.site_name
            parameter = req.parameter
            domain_name= req.domain_name
            self.key = redis_client.build_key(crawler_name, parameter, domain_name)
            cached_response = redis_client.get_crawler_response(self.key)
            serialized_req = RequestSerializer(req)
            if cached_response:
                return apiResponse({'request': serialized_req.data, 'response': cached_response, 'detail': 'Cached response returned'})
            print(serialized_req)
            send_live_request_to_queue(serialized_req.data, req.site_name)
            
            timeout_seconds = 120
            interval = 2
            elapsed = 0
            while elapsed < timeout_seconds:
                cached_response = redis_client.get_crawler_response(self.key)
                if cached_response:
                    return apiResponse({'request': serialized_req.data , 'response': cached_response, 'detail': 'Fresh response returned'})
                sleep(interval)
                elapsed += interval
            
            return apiResponse({'requestId': str(req.request_id), 'detail': 'Request accepted; response processing in progress'}, status=202)
        else:
            return apiResponse(serializer.errors, status=400)