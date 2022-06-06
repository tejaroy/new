from django.db import models
from views import manager

class Manager1(models.Model):
    username = models.CharField(max_length=50)
    #employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Employee1(models.Model):
    name = models.CharField(max_length=25)
    manager = models.ForeignKey(Manager1, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Teja(models.Model):
    name = models.CharField(max_length=25)
# Create your models here.
