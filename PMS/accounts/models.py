from django.db import models


# Create your models here.
#translate to form view
class StudentInfo(models.Model):
    #student_id = models.CharField(primary_key=True, max_length=50)
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
        # return self.student_id
        return self.lastname