from django.db import models
from accounts.models import StudentInfo


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
    amount = models.FloatField(default=0.0)

    def __unicode__(self):
        return unicode(self.receipt_id)


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=50, blank=False)
    project_receiver = models.CharField(max_length=100, blank=False)
    project_cost = models.FloatField(default=0.0)

    def __unicode__(self):
        return unicode(self.project_id)
        