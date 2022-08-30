from django.contrib import admin

# Register your models here.
from .models import Job

# Allows us to change/add data without touching database
admin.site.register(Job)