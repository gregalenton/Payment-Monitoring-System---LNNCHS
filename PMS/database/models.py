from django.db import models
from django.contrib.auth.models import User


class Admin(models.Model):
    admin_user = models.OneToOneField(User, related_name='admin')
    admin_num = models.IntegerField(default=0)


class Due(models.Model):
    due_name = models.CharField(max_length=45, blank=False)
    due_cost = models.FloatField(default=0.0)


class Guardian(models.Model):
    guardian_name = models.CharField(max_length=100, blank=False)
    guardian_address = models.CharField(max_length=100, blank=False)
    guardian_contact = models.CharField(max_length=20, blank=False)


class Scholarship(models.Model):
    scholarship_name = models.CharField(max_length=50, blank=False)


class Project(models.Model):
    project_name = models.CharField(max_length=50, blank=False)
    project_receiver = models.CharField(max_length=100, blank=False)
    project_cost = models.FloatField(default=0.0)


class Disbursement(models.Model):
    disbursement_project = models.ForeignKey(Project, blank=False)
    disbursement_cost = models.FloatField(default=0.0)


class Student(models.Model):
    G7 = "7"
    G8 = "8"
    G9 = "9"
    G0 = "10"
    G1 = "11"
    G2 = "12"
    year_level = (
        (G7, 'grade 7'),
        (G8, 'grade 8'),
        (G9, 'grade 9'),
        (G0, 'grade 10'),
        (G1, 'grade 11'),
        (G2, 'grade 12'),
    )
    section = (
        ('A', 'section A'),
        ('B', 'section B'),
        ('C', 'section C'),
        ('D', 'section D'),
        ('E', 'section E'),
        ('F', 'section F'),
        ('G', 'section G'),
        ('H', 'section H'),
        ('I', 'section I'),
        ('J', 'section J'),
        ('K', 'section K'),
        ('L', 'section L'),
        ('M', 'section M'),
        ('N', 'section N'),
        ('SA', 'Ssection A'),
        ('SB', 'Ssection B'),
    )
    student_user = models.OneToOneField(User, related_name='student')
    student_year = models.IntegerField(choices=year_level, blank=False)
    student_section = models.CharField(max_length=2, choices=section, blank=False)
    student_address = models.CharField(max_length=100, blank=False)
    student_guardian = models.ForeignKey(Guardian, null=False, blank=False)
    student_scholarship = models.ForeignKey(Scholarship, null=True, blank=True)
    student_sibling = models.ManyToManyField("self")
    student_bandMem = models.BooleanField(default=False)
    student_payed = models.FloatField(default=0.0)
    student_toPay = models.FloatField(default=0.0)

