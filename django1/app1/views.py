from django.shortcuts import render, redirect
from .forms import GithubURLForm
from .models import GithubURL

def submit_url(request):
    if request.method == "POST":
        form = GithubURLForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = GithubURLForm()
    return render(request, 'app1/input_form.html', {'form': form})

def success(request):
    return render(request, 'app1/success.html')
