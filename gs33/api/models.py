from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=78)
    city = models.CharField(max_length=78)
    passbywhome = models.CharField(max_length=78)    
    roll = models.IntegerField(max_length=78)