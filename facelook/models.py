from django.db import models
from datetime import datetime,date
# Create your models here.
class EmployeeModels(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Password = models.CharField(max_length=32,default='12345')
    Department = models.CharField(max_length=50,default=None)
    Mail = models.EmailField()
    Post = models.CharField(max_length=30,default=None)
    Address = models.CharField(max_length=100)
    City = models.CharField(max_length=30)
    Attendance = models.IntegerField(default=0)
    Start_date = models.DateField(default=date.today())
    Salary = models.IntegerField()
    Age = models.IntegerField()
class live_attendance(models.Model):
    Id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Department = models.CharField(max_length=50,default=None)
    Post = models.CharField(max_length=30,default=None)
    Date = models.CharField(max_length=40,default=date.today())
    Time = models.CharField(max_length=40,default=str(datetime.now())[11:19])
