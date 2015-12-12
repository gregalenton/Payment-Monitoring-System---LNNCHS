from django.db import models
from accounts.models import Student


class Due(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=False)
    cost = models.FloatField(default=0.0)


class Receipt(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(blank=True, auto_now_add=True)
    student_id = models.ForeignKey(Student)
    payment = models.IntegerField(default=0, blank=False)


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False)
    receiver = models.CharField(max_length=100, blank=False)
    cost = models.FloatField(default=0.0)


class Disbursement(models.Model):
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, blank=False)
    cost = models.FloatField(default=0.0)