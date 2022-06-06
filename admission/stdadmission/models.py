from django.db import models
from django.forms import CharField  

class Student(models.Model):  
 
    rollno = models.CharField(max_length=100)  
    name = models.CharField(max_length=15)  
    age=models.IntegerField(max_length=2)
    city=models.CharField(max_length=15)
    stdclass=models.CharField(max_length=12)
    class Meta:  
        db_table = "student"  