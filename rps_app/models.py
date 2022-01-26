from django.db import models

class User(models.Model):
    User_Name= models.CharField(max_length=100)
    Mail_id= models.CharField(max_length=100)
    password=models.CharField(max_length=15)

