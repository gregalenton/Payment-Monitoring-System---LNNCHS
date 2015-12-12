from django.db import models
from django.contrib.auth.models import User


class Admin(models.Model):
    user = models.OneToOneField(User, related_name='admin')
    num = models.IntegerField(default=0)


class Student(models.Model):
    G7 = "7"
    G8 = "8"
    G9 = "9"
    G0 = "10"
    G1 = "11"
    G2 = "12"
    YEAR_LEVELS = (
        (G7, 'grade 7'),
        (G8, 'grade 8'),
        (G9, 'grade 9'),
        (G0, 'grade 10'),
        (G1, 'grade 11'),
        (G2, 'grade 12'),
    )
    SECTION_CHOICE = (
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
    SCHOLARSHIP_CHOICES = (
        ('Academic', 'Academic Scholar'),
        ('Athletic', 'Athletic Scholar')
    )

    user = models.OneToOneField(User, related_name='student')
    year = models.IntegerField(choices=YEAR_LEVELS, blank=False)
    section = models.CharField(max_length=2, choices=SECTION_CHOICE, blank=False)
    address = models.CharField(max_length=100, blank=False)
    guardian_firstname = models.CharField(max_length=50)
    guardian_lastname = models.CharField(max_length=50)
    guardian_contact = models.CharField(max_length=100)
    guardian_address = models.CharField(max_length=100)
    scholarship = models.CharField(max_length=100, choices=SCHOLARSHIP_CHOICES, null=True, blank=True)
    sibling = models.BooleanField(default=False)
    bandMem = models.BooleanField(default=False)
    paid = models.FloatField(default=0.0)
    toPay = models.FloatField(default=0.0)