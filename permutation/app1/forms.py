from django import forms
class inputform(forms.Form):
    name=forms.CharField(max_length=4)
    