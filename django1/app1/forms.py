from django import forms
from .models import GithubURL

class GithubURLForm(forms.ModelForm):
    class Meta:
        model = GithubURL
        fields = ['url1']
