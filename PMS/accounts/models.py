from django.db import models
from django.contrib.auth.models import User

# Create your models here.
GENDER = (
    ('M', 'Male'),
    ('F', 'Female')
)
MIN_VALID_AGE = 15
Valid_Gender = []
for Gender in GENDER:
    Valid_Gender.append(Gender[0])
    Valid_Gender.sort()


class StudentInfo(models.Model):
    user = models.OneToOneField(User)
    student_id = models.CharField(
        primary_key=True,
        verbose_name='student ID', 
        max_length=50
    )
    
    lastname = models.CharField(
        verbose_name='last name',
        max_length=50
    )
    
    firstname = models.CharField(
        verbose_name='first name',
        max_length=50
    )

    middlename = models.CharField(
        verbose_name='middle name',
        max_length=50
    )
    
    gender = models.CharField(
        max_length=2,
        choices=GENDER,
        blank=True,
        null=True
    )

    birthday = models.DateField(
        verbose_name='birthday',
        blank=True, 
        null=True
    )

    def __unicode__(self):
        return self.student_id

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            StudentInfo.objects.create(user=instance)

    class Meta:
        db_table = 'Student_User'
        verbose_name = 'Student User'
        verbose_name_plural = 'Student Users'