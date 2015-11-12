from django.db import models

class StudentInfo(models.Model):
    student_id = models.AutoField(primary_key=True)
    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50)
    birthday = models.DateField(blank=True, null=True)

    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    gender = models.CharField(
        max_length=2,
        choices=GENDER,
        blank=True,
        null=True
    )

    def __unicode__(self):
        return unicode(self.student_id)