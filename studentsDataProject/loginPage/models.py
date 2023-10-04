from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length= 200)
    last_name =  models.CharField(max_length= 200) 
    emailId =  models.CharField(max_length= 200)
    password =  models.CharField(max_length= 200)
