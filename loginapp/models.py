from django.db import models

# Create your models here.
class User(models.Model):
    id=models.AutoField(primary_key=True)
    fname=models.CharField(max_length= 100)
    lname=models.CharField(max_length= 100)
    email=models.CharField(max_length= 100)
    password=models.CharField(max_length= 100)
    cpassword=models.CharField(max_length= 100)

class StuUser(models.Model):
    id=models.AutoField(primary_key=True)
    fname=models.CharField(max_length= 100)
    lname=models.CharField(max_length= 100)
    roll=models.CharField(max_length= 100)
    email=models.CharField(max_length= 100)
    password=models.CharField(max_length= 100)
    cpassword=models.CharField(max_length= 100)

class CourseCreate(models.Model):
    id=models.AutoField(primary_key=True)
    tname=models.CharField(max_length= 100)
    qualification=models.CharField(max_length= 100)
    coursename=models.CharField(max_length= 100)

class Ass_Create(models.Model):
    id=models.AutoField(primary_key=True)
    cname=models.CharField(max_length= 100)
    topic=models.CharField(max_length= 100)
    question=models.CharField(max_length= 1000)
    document = models.FileField(upload_to='media')
    time=models.CharField(max_length= 100)

    
class EX_Create(models.Model):
    id=models.AutoField(primary_key=True)
    ename=models.CharField(max_length= 100)
    topic=models.CharField(max_length= 100)
    description=models.CharField(max_length= 1000)
    document = models.FileField(upload_to='media')
    time=models.CharField(max_length= 100)

class Submit_Ass(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length= 100)
    roll=models.CharField(max_length= 100)
    topic=models.CharField(max_length= 100)
    document = models.FileField(upload_to='media')
    time=models.TimeField(auto_now=True)
    date=models.DateField(auto_now=True)

class Submit_exam(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length= 100)
    roll=models.CharField(max_length= 100)
    topic=models.CharField(max_length= 100)
    document = models.FileField(upload_to='media')
    time=models.TimeField(auto_now=True)
    date=models.DateField(auto_now=True)

class Ass_Grade(models.Model):
    id=models.AutoField(primary_key=True)
    roll=models.CharField(max_length= 100)
    cname=models.CharField(max_length= 100)
    obmark=models.CharField(max_length= 100)
    tomark=models.CharField(max_length= 100)
   

class Ex_Grade(models.Model):
    id=models.AutoField(primary_key=True)
    roll=models.CharField(max_length= 100)
    cname=models.CharField(max_length= 100)
    obmark=models.CharField(max_length= 100)
    tomark=models.CharField(max_length= 100)
   

