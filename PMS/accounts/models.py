from django.db import models


class StudentInfo(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_lastname = models.CharField(max_length=50)
    student_firstname = models.CharField(max_length=50)
    student_middlename = models.CharField(max_length=50)
    student_birthday = models.DateField(blank=True, null=True)

    G7 = "7"
    G8 = "8"
    G9 = "9"
    G0 = "10"
    G1 = "11"
    G2 = "12"
    YEAR_LEVEL = (
        (G7, 'grade 7'),
        (G8, 'grade 8'),
        (G9, 'grade 9'),
        (G0, 'grade 10'),
        (G1, 'grade 11'),
        (G2, 'grade 12'),
    )

    student_year = models.CharField(choices=YEAR_LEVEL, max_length=30, blank=True)

    SECTION = (
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

    student_section = models.CharField(max_length=2, choices=SECTION, blank=False)

    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    student_gender = models.CharField(
        max_length=2,
        choices=GENDER,
        blank=True,
        null=True
    )

    student_address = models.CharField(max_length=100)
    student_guardian = models.CharField(max_length=100)
    student_guardian_contact = models.CharField(max_length=100)
    student_guardian_address = models.CharField(max_length=100)
    student_scholarship = models.CharField(max_length=100, null=True, blank=True)
    student_sibling = models.BooleanField(default=False)
    student_bandMem = models.BooleanField(default=False)
    student_paid = models.FloatField(default=0.0)
    student_toPay = models.FloatField(default=0.0)

    def __unicode__(self):
        return unicode(self.student_id)

