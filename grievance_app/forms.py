from django import forms
from .models import Grievance
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class GrievanceForm(forms.ModelForm):
    class Meta:
        model = Grievance
        fields = [
            'name',
            'email',
            'complaint',
            'photo',
            'latitude',
            'longitude',
        ]

        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']