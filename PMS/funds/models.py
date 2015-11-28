from django.db import models
from accounts.models import StudentInfo

# class Funds(models.Model):

#     """Sets the Fund details"""

#     fund_id = models.AutoField(primary_key=True)	
#     fund_name = models.CharField(max_length=255)
#     fund_timestamp = models.DateTimeField(blank=True, auto_now_add=True)
#     fund_amount = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
# 		return self.fund_id

class Due(models.Model):
    due_id = models.AutoField(primary_key=True)
    due_name = models.CharField(max_length=45, blank=False)
    due_cost = models.FloatField(default=0.0)

    def __unicode__(self):
        return unicode(self.due_id)


class Receipt(models.Model):
    receipt_id = models.AutoField(primary_key=True)
    receipt_timestamp = models.DateTimeField(blank=True, auto_now_add=True)
    student_id = models.ForeignKey(StudentInfo)
    due_id = models.ForeignKey(Due)

    def __unicode__(self):
        return unicode(self.project_id)


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=50, blank=False)
    project_receiver = models.CharField(max_length=100, blank=False)
    project_cost = models.FloatField(default=0.0)

    def __unicode__(self):
        return unicode(self.project_id)


class Disbursement(models.Model):
    disbursement_id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey(Project, blank=False)
    disbursement_cost = models.FloatField(default=0.0)

    def __unicode__(self):
        return unicode(disbursement_id)