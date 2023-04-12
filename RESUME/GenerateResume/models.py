from django.db import models

# Create your models here.

class userinfo(models.Model):
    uid = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    about = models.CharField(max_length=100)
    mail=models.CharField(max_length=30,default='nogmail')

class skills(models.Model):
    uid = models.CharField(max_length=10)
    skillname = models.CharField(max_length=20)


class languages(models.Model):
    uid = models.CharField(max_length=10)
    langname = models.CharField(max_length=20)


class projects(models.Model):
    uid = models.CharField(max_length=10)
    proj = models.CharField(max_length=20)


class specializations(models.Model):
    uid = models.CharField(max_length=10)
    specname = models.CharField(max_length=20)


class workexp(models.Model):
    uid = models.CharField(max_length=10)
    workname = models.CharField(max_length=20)