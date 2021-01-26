from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    university = models.CharField(max_length=1000)
    skill = models.CharField(max_length=1000)
    about_you = models.CharField(max_length=100)
    previous_work = models.CharField(max_length=100)
