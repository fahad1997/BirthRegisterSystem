from django.db import models
from django.utils import timezone


class NewChildInfo(models.Model):
    Name = models.CharField(max_length=100)
    Birth_Date = models.DateTimeField(default=timezone.now)
    Blood_group = models.CharField(max_length=10)
    Father_name = models.CharField(max_length=50)
    Father_NID = models.CharField(max_length=20)
    Mother_name = models.CharField(max_length=50)
    Religion = models.CharField(max_length=20)
    Validation = models.BooleanField(default=False)
    District_name = models.CharField(max_length=50)
    Division_name = models.CharField(max_length=50)
    Upazila_name = models.CharField(max_length=50)
    Union_name = models.CharField(max_length=50)
