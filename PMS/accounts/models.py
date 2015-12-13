from django.db import models
from django.contrib.auth.models import User


class Admin(models.Model):
    user = models.OneToOneField(User, related_name='admin')
    num = models.IntegerField(default=0)


class Student(models.Model):
    YEAR_LEVELS = (
        (7, 'Grade 7'),
        (8, 'Grade 8'),
        (9, 'Grade 9'),
        (0, 'Grade 10'),
        (1, 'Grade 11'),
        (2, 'Grade 12'),
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
    bandMem = models.BooleanField(default=False, blank=False)
    paid = models.FloatField(default=0.0)
    toPay = models.FloatField(default=0.0)