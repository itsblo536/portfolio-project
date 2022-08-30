from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField()
    body = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/')

#Create a Blog models
#title
#publication date
#body
#image

#Add the blog app to the settings


# Create a migration

# Migrate

# Add to the admin