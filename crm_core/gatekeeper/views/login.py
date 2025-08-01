from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from ..forms import LoginForm  # adjust the import path as needed
from django.http import HttpResponse
class Login(View):
    
    template_name = "gatekeeper\html\login.html"
    
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        error = None
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('jobhub:home')  
            else:
                error = "Invalid username or password."
        return render(request, self.template_name, {'form': form, 'error': error})
