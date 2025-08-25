from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from ..forms import JobCreateForm
from gatekeeper.models.user import User

class Job(View):

    template_name = "jobhub/html/createjob.html"  

    def get(self, request, *args, **kwargs):
        client_email = request.user.email
        form = JobCreateForm(client_email=client_email)
        return render(request, self.template_name, {'form': form})
        

    def post(self, request, *args, **kwargs):
        client_email = request.user.email
        domain_id = request.POST.get('domain')
        form = JobCreateForm(request.POST, client_email=client_email, domain_id = domain_id)

        if form.is_valid():
            job = form.save(commit=False)

            try:
                client_user = User.objects.get(email=form.cleaned_data['client'])
            except User.DoesNotExist:
                return HttpResponse("Invalid client email", status=400)

            job.client = client_user
            job.save()
            return HttpResponse("Job Created Successfully")
        else:
            return render(request, self.template_name, {'form': form})