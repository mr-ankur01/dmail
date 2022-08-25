
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserEmail(models.Model):
    address=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    acc_id=models.CharField(max_length=100)
    
class Inbox(models.Model):
    senderName=models.CharField(max_length=122)
    senderEmail=models.CharField(max_length=122)
    subject=models.CharField(max_length=122)
    date=models.CharField(max_length=122)
    mailBody=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    to=models.CharField(max_length=122)
    fileName=models.CharField(max_length=120,null=True)
    size=models.CharField(max_length=120,null=True)
    file=models.FileField(upload_to='files' ,null=True)
    
class ForgetUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    token = models.CharField(max_length=122)
    date = models.DateTimeField(auto_now_add=True)    