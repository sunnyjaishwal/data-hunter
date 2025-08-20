from rest_framework.views import APIView
from rest_framework.response import Response as apiResponse
from ..serializers.request import RequestSerializer
from ..task import send_live_request_to_queue
from rest_framework.throttling import UserRateThrottle
from ..throttling import UserCrawlerRateThrottle 


class Airline(APIView):

    throttle_classes = [UserRateThrottle, UserCrawlerRateThrottle]

    def post(self, request):
        data = request.data.copy()
        data['domain_name'] = 'airline'
        serializer = RequestSerializer(data=data)
        if serializer.is_valid():
            req = serializer.save()
            print("request daved in model and processing to queue")
            send_live_request_to_queue(req.request_id, req.crawler_name)
            return apiResponse({'requestId': str(req.request_id), 'detail': 'Request accepted and enqueued'})
        else:
            return apiResponse(serializer.errors, status=400)