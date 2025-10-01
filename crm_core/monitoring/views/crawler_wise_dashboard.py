from django.views import View
from django.shortcuts import render, redirect 
from ..forms import CrawlerWiseViewForm
from crawler.models import Crawler  
from crm_core.mongo_db_service import client
import os

class CrawlerWiseDashboard(View):
    template = 'monitoring/html/crawler_wise_dashboard.html'
    
    def get(self, request):
        form = CrawlerWiseViewForm()
        return render(request, self.template, {'form': form})
    
    def post(self, request):
        form = CrawlerWiseViewForm(request.POST)
        context = {'form': form}
        
        if form.is_valid():
            selected_crawler = str(form.cleaned_data['crawler'])
            
            try:
                # crawler = Crawler.objects.get(id=selected_crawler)
                # Connect to MongoDB and get request count
                db = client[os.getenv('MONGO_DB_NAME')]
                collection = db['request_in']
                # Count documents where site_name matches crawler name
                request_count = collection.count_documents({"request.site_name": selected_crawler})
                
                context.update({
                    'selected_crawler': selected_crawler,
                    'request_count': request_count
                })
            except Crawler.DoesNotExist:
                context['error'] = "Selected crawler not found"
            except Exception as e:
                context['error'] = f"Error fetching data: {str(e)}"
        return render(request, self.template, context)
    
    