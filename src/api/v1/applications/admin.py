from django.contrib import admin

# Register your models here.
from .models import Application, Job, JobHeader


admin.site.register(Application)

admin.site.register(Job)

admin.site.register(JobHeader)
