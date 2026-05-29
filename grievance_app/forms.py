from django import forms
from .models import Grievance

class GrievanceForm(forms.ModelForm):
    class Meta:
        model = Grievance
        fields = ['name', 'email', 'complaint']