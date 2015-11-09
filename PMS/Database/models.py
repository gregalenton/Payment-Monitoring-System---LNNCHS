from django.db import models
from django.contrib.auth.models import User


class Admin(models.Model):
    admin_user = models.OneToOneField(User, related_name='admin')
    admin_num = models.IntegerField(default=0)


class Due(models.Model):
    due_name = models.CharField(max_length=45)
    due_cost = models.FloatField(default=0.0)


class Guardian(models.Model):
    guardian_name = models.CharField(max_length=100)
    guardian_address = models.CharField(max_length=100)
    guardian_contact = models.CharField(max_length=20)


class Scholarship(models.Model):
    scholarship_name = models.CharField(max_length=50)


class Project(models.Model):
    project_name = models.CharField(max_length=50)
    project_receiver = models.CharField(max_length=100)
    project_cost = models.FloatField(default=0.0)


class Disbursement(models.Model):
    disbursement_project = models.ForeignKey(Project)
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
    student_user = models.OneToOneField(User, related_name='student', unique=True)
    student_year = models.IntegerField(choices=year_level)
    student_section = models.CharField(max_length=2, choices=section)
    student_address = models.CharField(max_length=100)
    student_guardian = models.ForeignKey(Guardian)
    student_sibling = models.ManyToManyField("self")
    student_bandMem = models.BooleanField(default=False)
    student_payed = models.FloatField(default=0.0)
    student_toPay = models.FloatField(default=0.0)

