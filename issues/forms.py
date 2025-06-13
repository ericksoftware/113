from django import forms
from .models import Issue, Status
from django.contrib.auth import get_user_model
from accounts.models import Team

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = [
            'title', 'summary', 'description', 
            'assignee', 'status', 'assigned_team'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assignee'].queryset = get_user_model().objects.all()
        self.fields['status'].queryset = Status.objects.all()
        self.fields['assigned_team'].queryset = Team.objects.all()