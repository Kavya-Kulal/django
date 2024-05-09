from django import forms
class inputform(forms.Form):
    name=forms.CharField(max_length=10)
    college=forms.CharField(max_length=10,label="college")
    course=forms.CharField(max_length=10,label="corse")

