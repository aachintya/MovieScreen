from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Show

class ShowForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = ['movie', 'time', 'uuid']
