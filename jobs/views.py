from django.shortcuts import render

from .models import Job
from .models import Edu
from .models import Skills
from .models import Projects

def home(request):
    jobs = Job.objects
    edus = Edu.objects
    skills = Skills.objects
    projects = Projects.objects
    return render(request, 'jobs/home.html', {'jobs':jobs, 'edus':edus, 'skills':skills, 'projects':projects})
