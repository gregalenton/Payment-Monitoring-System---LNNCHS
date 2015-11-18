from django.db import models


class Due(models.Model):
    due_name = models.CharField(max_length=45, blank=False)
    due_cost = models.FloatField(default=0.0)


class Project(models.Model):
    project_name = models.CharField(max_length=50, blank=False)
    project_receiver = models.CharField(max_length=100, blank=False)
    project_cost = models.FloatField(default=0.0)


class Disbursement(models.Model):
    disbursement_project = models.ForeignKey(Project, blank=False)
    disbursement_cost = models.FloatField(default=0.0)