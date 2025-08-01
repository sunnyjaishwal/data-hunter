from django import forms
from gatekeeper.models.user import User
from .models.job import Job, JobType, ClientJobPermission

class JobCreateForm(forms.ModelForm):
    title = forms.CharField(max_length=255, label="Job Title")
    client = forms.CharField()
    job_type = forms.ModelChoiceField(queryset=JobType.objects.none(),label="Job Type")
    website = forms.CharField(max_length=255, required=False, label="Website (optional)")
    status = forms.CharField(max_length=50, initial='pending', widget=forms.HiddenInput())
    
    class Meta:
        model = Job
        exclude = ['client']  

    def __init__(self, *args, **kwargs):
        client_email = kwargs.pop('client_email', None)
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
        else:
            # If no client_email passed, no job types available
            self.fields['job_type'].queryset = JobType.objects.none()

