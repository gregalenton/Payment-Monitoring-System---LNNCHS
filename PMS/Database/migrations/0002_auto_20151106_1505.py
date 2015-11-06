# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Sibling',
        ),
        migrations.RenameField(
            model_name='admin',
            old_name='email_add',
            new_name='admin_email_add',
        ),
        migrations.RenameField(
            model_name='admin',
            old_name='password',
            new_name='admin_password',
        ),
        migrations.RenameField(
            model_name='admin',
            old_name='username',
            new_name='admin_username',
        ),
        migrations.RenameField(
            model_name='disbursement',
            old_name='total_cost',
            new_name='disbursement_cost',
        ),
        migrations.RenameField(
            model_name='disbursement',
            old_name='project',
            new_name='disbursement_project',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='cost',
            new_name='project_cost',
        ),
        migrations.RenameField(
            model_name='receipt',
            old_name='date',
            new_name='receipt_date',
        ),
        migrations.RenameField(
            model_name='receipt',
            old_name='due',
            new_name='receipt_due',
        ),
        migrations.RenameField(
            model_name='receipt',
            old_name='student',
            new_name='receipt_student',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='username',
            new_name='student_section',
        ),
        migrations.RemoveField(
            model_name='disbursement',
            name='disbursement_id',
        ),
        migrations.RemoveField(
            model_name='due',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='due',
            name='due_id',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_number',
        ),
        migrations.RemoveField(
            model_name='project',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='receipt',
            name='id',
        ),
        migrations.RemoveField(
            model_name='scholarship',
            name='scholarship_id',
        ),
        migrations.RemoveField(
            model_name='student',
            name='password',
        ),
        migrations.AddField(
            model_name='due',
            name='due_cost',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='project',
            name='project_receiver',
            field=models.CharField(default=b'person', max_length=45),
        ),
        migrations.AddField(
            model_name='student',
            name='student_address',
            field=models.CharField(default=b'n/a', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='student_bandMember',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='student_currentPaid',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='student',
            name='student_guardian',
            field=models.ForeignKey(default=b'NULL', to='Database.Guardian'),
        ),
        migrations.AddField(
            model_name='student',
            name='student_password',
            field=models.CharField(default=b'password', max_length=32),
        ),
        migrations.AddField(
            model_name='student',
            name='student_scholarship',
            field=models.ForeignKey(default=b'NULL', to='Database.Scholarship'),
        ),
        migrations.AddField(
            model_name='student',
            name='student_siblings',
            field=models.ManyToManyField(related_name='_student_siblings_+', to='Database.Student'),
        ),
        migrations.AddField(
            model_name='student',
            name='student_status',
            field=models.CharField(default=b'NE', max_length=2, choices=[(b'ER', b'Enrolled'), (b'NE', b'NotEnrolled')]),
        ),
        migrations.AddField(
            model_name='student',
            name='student_toPay',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='student',
            name='student_username',
            field=models.CharField(default=b'stud', max_length=45),
        ),
        migrations.AddField(
            model_name='student',
            name='student_year',
            field=models.CharField(default=b'7', max_length=2, choices=[(b'7', b'Grade 7'), (b'8', b'Grade 8'), (b'9', b'Grade 9'), (b'10', b'Grade 10'), (b'11', b'Grade 11'), (b'12', b'Grade 12')]),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_name',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='receipt_no',
            field=models.CharField(max_length=15, serialize=False, primary_key=True),
        ),
    ]
