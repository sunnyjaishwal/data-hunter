from rest_framework.views import APIView
from rest_framework.response import Response as apiResponse
from ..serializers.request import RequestSerializer
from ..task import send_live_request_to_queue

class Hotel(APIView):
    
    def post(self, request):
        data = request.data.copy()
        data['domain_name'] = 'hotel'
        serializer = RequestSerializer(data=data)
        if serializer.is_valid():
            req = serializer.save()
            send_live_request_to_queue(req.request_id, req.crawler_name)
            return apiResponse({'request_id': str(req.request_id), 'detail': 'Request accepted and enqueued'})
        else:
            return apiResponse(serializer.errors, status=400)