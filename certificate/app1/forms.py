from django import forms
class inputform(forms.Form):
    name=forms.CharField(max_length=10,label="enter the name")
    college=forms.CharField(max_length=10,label="enter the college")
    course=forms.CharField(max_length=10,label="enter the course")

