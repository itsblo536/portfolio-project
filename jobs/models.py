from django.db import models

# models.Modle allows us to create class and gives us background stuff that allows this object to be saved in database
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
