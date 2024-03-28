from django.db import models

class Hydjobs1(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=30)
    title=models.CharField(max_length=30)
    address=models.TextField()
    email=models.EmailField()
    phonenumber=models.BigIntegerField()

class Bngjobs1(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=30)
    title=models.CharField(max_length=30)
    address=models.TextField()
    email=models.EmailField()
    phonenumber=models.BigIntegerField()

class Punejobs1(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=30)
    title=models.CharField(max_length=30)
    address=models.TextField()
    email=models.EmailField()
    phonenumber=models.BigIntegerField()

# Create your models here.
