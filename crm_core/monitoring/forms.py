from django import forms
from crawler.models import Crawler

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True, label = 'Username')
    password = forms.CharField(widget=forms.PasswordInput, required=True, label = 'Password')
    
class CrawlerWiseViewForm(forms.Form):
    crawler = forms.ModelChoiceField(queryset=Crawler.objects.all(), required=True, label='Select Crawler')