# forms.py
from django import forms
from .models import SpokenText

class SpokenTextForm(forms.ModelForm):
    class Meta:
        model = SpokenText
        fields = ['text']  # Specify the fields you want to include in the form
