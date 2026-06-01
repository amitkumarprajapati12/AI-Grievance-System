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
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            }),

            'complaint': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your complaint here',
                'rows': 4
            }),

            'photo': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),

            'latitude': forms.HiddenInput(),

            'longitude': forms.HiddenInput(),
        }


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email'
        })
    )

    class Meta:
        model = User

        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]