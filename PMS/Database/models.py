from django.db import models


class Admin(models.Model):
    admin_username = models.CharField(max_length=16)
    admin_email_add = models.EmailField(max_length=255)
    admin_password = models.CharField(max_length=32)


class Project(models.Model):
    project_name = models.CharField(max_length=45)
    project_receiver = models.CharField(max_length=45)
    project_cost = models.FloatField()


class Disbursement(models.Model):
    disbursement_project = models.ForeignKey(Project)
    disbursement_cost = models.FloatField()


class Due(models.Model):
    due_name = models.CharField(max_length=45)
    due_cost = models.FloatField()


class Guardian(models.Model):
    guardian_name = models.CharField(max_length=100)
    guardian_address = models.CharField(max_length=100)
    guardian_contact = models.CharField(max_length=20)


class Scholarship(models.Model):
    scholarship_name = models.CharField(max_length=50)


class Student(models.Model):
    G7 = '7'
    G8 = '8'
    G9 = '9'
    G0 = '10'
    G1 = '11'
    G2 = '12'
    ENROLLED = 'ER'
    NOT_ENROLLED = 'NE'
    student_username = models.CharField(max_length=45)
    student_password = models.CharField(max_length=32)
    student_name = models.CharField(max_length=100)
    year_level = (
        (G7, 'Grade 7'),
        (G8, 'Grade 8'),
        (G9, 'Grade 9'),
        (G0, 'Grade 10'),
        (G1, 'Grade 11'),
        (G2, 'Grade 12'),
    )
    student_year = models.CharField(max_length=2,
                                    choices=year_level,
                                    default=G7)
    student_section = models.CharField(max_length=45)
    student_address = models.CharField(max_length=100)
    status = (
        (ENROLLED, 'Enrolled'),
        (NOT_ENROLLED, 'NotEnrolled'),
    )
    student_status = models.CharField(max_length=2,
                                      choices=status,
                                      default=NOT_ENROLLED)
    student_guardian = models.ForeignKey(Guardian)
    student_siblings = models.ManyToManyField("self")
    student_bandMember = models.BooleanField(default=False)
    student_scholarship = models.ForeignKey(Scholarship)
    student_currentPaid = models.FloatField()
    student_toPay = models.FloatField()


class Receipt(models.Model):
    receipt_no = models.CharField(max_length=15, primary_key=True)
    receipt_date = models.DateField()
    receipt_student = models.ForeignKey(Student)
    receipt_due = models.ForeignKey(Due)


