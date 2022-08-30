from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField()
    body = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/')

    # renames Blog objects as their title - easier to identify in admin page
    def __str__(self):
        return self.title

    # Caps body of text on home page to 100 words 
    def summary(self):
        return self.body[:100]

#Create a Blog models
#title
#publication date
#body
#image

#Add the blog app to the settings


# Create a migration

# Migrate

# Add to the admin