from django.db import models

# Create your models here.
class nikeApp(models.Model):
    firstname = models.CharField(max_length=225)
    lastname = models.CharField(max_length=255)
    jobtitle = models.CharField(max_length=255)
    

