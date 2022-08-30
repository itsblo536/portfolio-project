from django.shortcuts import render

from .models import Job

# Job apps will be used on homepage
def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs': jobs})
