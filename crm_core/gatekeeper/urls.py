from django.urls import path
from .views.registration import Registration
from .views.login import Login

urlpatterns = [
    path('registration/', Registration.as_view(), name='registration'),
    path('login/', Login.as_view(), name='login'),
]