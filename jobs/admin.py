from django.contrib import admin

from .models import Job
from .models import Edu
from .models import Skills
from .models import Projects

admin.site.register(Job)
admin.site.register(Edu)
admin.site.register(Skills)
admin.site.register(Projects)
