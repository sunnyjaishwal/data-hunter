from django.urls import path
from .views.login import Login
from .views.home import Home
from .views.crawler_wise_dashboard import CrawlerWiseDashboard
app_name = 'monitoring'

urlpatterns = [
    path('login/', Login.as_view(), name='Login'),
    path('home/', Home.as_view(), name='Home'),
    path('crawler-wise-dashboard/', CrawlerWiseDashboard.as_view(), name='CrawlerWiseDashboard'),
]