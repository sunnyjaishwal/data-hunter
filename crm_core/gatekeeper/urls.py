from django.urls import path
from .views.registration import Registration
from .views.login import Login
from .views.change_password import ChangePassword

urlpatterns = [
    path('registration/', Registration.as_view(), name='registration'),
    path('login/', Login.as_view(), name='login'),
    path('changepassword/', ChangePassword.as_view(), name= 'change password')
]