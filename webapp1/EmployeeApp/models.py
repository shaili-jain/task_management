from django.db import models

# Create your models here.

class User(models.Model):
    u_id = models.CharField(primary_key=True,max_length=20)
    uFName=models.CharField(max_length=50)
    uLName=models.CharField(max_length=50)
    uRole=models.CharField(max_length=40)
    uEmail=models.EmailField(max_length=100)
    uAvailableHr=models.IntegerField(default=8)
    uPassword=models.CharField(max_length=10)


class Task(models.Model):
    t_id= models.AutoField(primary_key=True)
    tName=models.CharField(max_length=100)
    tDescp=models.TextField(max_length=500)
    tPriority=models.IntegerField()
    tExpHr=models.IntegerField()
    u_id=models.ForeignKey(User,on_delete=models.CASCADE)

class Assign(models.Model):
    t_status=models.CharField(max_length=100,default="ToDo")
    assignDate=models.DateField()
    assignerName=models.CharField(max_length=100)
    assigneeId=models.ForeignKey(User,on_delete=models.CASCADE)
    t_id=models.ForeignKey(Task,on_delete=models.CASCADE)

