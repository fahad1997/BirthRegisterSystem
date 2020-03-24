from django.db import models


class Area(models.Model):
    District_name = models.CharField(max_length=50)
    Division_name = models.CharField(max_length=50)
    Upazila_name = models.CharField(max_length=50)
    Union_name = models.CharField(max_length=50)


class UpAdmin(models.Model):
    District_name = models.CharField(max_length=50)
    Division_name = models.CharField(max_length=50)
    Upazila_name = models.CharField(max_length=50)
    U_username = models.CharField(max_length=50)
    U_password = models.CharField(max_length=50)


class Hospital(models.Model):
    H_name = models.CharField(max_length=50)
    District_name = models.CharField(max_length=50)
    Division_name = models.CharField(max_length=50)
    Upazila_name = models.CharField(max_length=50)
    Union_name = models.CharField(max_length=50)
    H_username = models.CharField(max_length=50)
    H_password = models.CharField(max_length=50)


class AddDistrict(models.Model):
    AddDistrict=models.CharField(max_length=50)