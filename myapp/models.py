from django.db import models

# Create your models here.
class Employee(models.Model):
    empid=models.IntegerField(primary_key=True)
    empname=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    salary=models.IntegerField()