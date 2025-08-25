from django import forms
from gatekeeper.models.user import User
from .models.job import Job, JobType, ClientJobPermission
from crawler.models import Crawler
from domain.models import Domain
from agreement.models import Agreement
class JobCreateForm(forms.ModelForm):
    title = forms.CharField(max_length=255, label="Job Title")
    client = forms.CharField()
    job_type = forms.ModelChoiceField(queryset=JobType.objects.none(),label="Job Type")
    domain = forms.ModelChoiceField(queryset = Domain.objects.none(), label='Domain Name')
    crawler = forms.ModelChoiceField(queryset= Crawler.objects.none(), label='Crawler Name')
    schedule_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), label="Schedule Time")
    status = forms.CharField(max_length=50, initial='pending', widget=forms.HiddenInput())
    
    class Meta:
        model = Job
        exclude = ['client']  

    def __init__(self, *args, **kwargs):
        client_email = kwargs.pop('client_email', None)
        domain_id = kwargs.pop('domain_id', None)
        super().__init__(*args, **kwargs)
        
        if client_email:
            # Set the client email as initial value and disable editing
            self.fields['client'].initial = client_email
            self.fields['client'].disabled = True
        
            try:
                client_user = User.objects.get(email=client_email)
            except User.DoesNotExist:
                    client_user = None

            if client_user:
                allowed_job_type_ids = ClientJobPermission.objects.filter(
                    client=client_user
                ).values_list('allowed_job_type_id', flat=True)
                self.fields['job_type'].queryset = JobType.objects.filter(id__in=allowed_job_type_ids)
            else:
                self.fields['job_type'].queryset = JobType.objects.none()
                
            # DOMAIN FILTER: get allowed domains for this user's company
            company = client_user.client_id
            allowed_domains = Agreement.objects.filter(company=company).values_list('allowed_domains', flat=True)
            self.fields['domain'].queryset = Domain.objects.filter(id__in = allowed_domains)
            allowed_crawlers = Agreement.objects.filter(company=company).values_list('allowed_crawlers', flat=True)
            self.fields['crawler'].queryset = Crawler.objects.filter(id__in= allowed_crawlers)
            
        else:
            # If no client_email passed, no job types available
            self.fields['job_type'].queryset = JobType.objects.none()

