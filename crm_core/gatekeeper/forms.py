from django import forms
from .models.user import User 
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True, label = 'Username')
    password = forms.CharField(widget=forms.PasswordInput, required=True, label = 'Password')


class ChangePasswordForm(forms.Form):
    username = forms.CharField(max_length=150, required=True, label='Username')
    old_password = forms.CharField(widget=forms.PasswordInput, required=True, label = 'Old Password')
    new_password = forms.CharField(widget=forms.PasswordInput, required=True, label = 'New Password')