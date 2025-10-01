from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from ..forms import LoginForm
# Create your views here.
class Login(View):
    template = 'monitoring/html/login.html'
    
    def get(self, request):
        form = LoginForm()
        return render(request, self.template, {'form': form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        error = None
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.user_type in ['admin', 'operations']:
                   login(request, user)
                   return redirect('monitoring:Home')
                else:
                    error = "You do not have permission to access this dashboard."
            else:
                error = "Invalid username or password."
        return render(request, self.template, {'form': form, 'error': error})
