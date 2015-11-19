# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('student_id', models.AutoField(serialize=False, primary_key=True)),
                ('student_lastname', models.CharField(max_length=50)),
                ('student_firstname', models.CharField(max_length=50)),
                ('student_middlename', models.CharField(max_length=50)),
                ('student_birthday', models.DateField(null=True, blank=True)),
                ('student_year', models.IntegerField(blank=True, choices=[(b'7', b'grade 7'), (b'8', b'grade 8'), (b'9', b'grade 9'), (b'10', b'grade 10'), (b'11', b'grade 11'), (b'12', b'grade 12')])),
                ('student_section', models.CharField(max_length=2, choices=[(b'A', b'section A'), (b'B', b'section B'), (b'C', b'section C'), (b'D', b'section D'), (b'E', b'section E'), (b'F', b'section F'), (b'G', b'section G'), (b'H', b'section H'), (b'I', b'section I'), (b'J', b'section J'), (b'K', b'section K'), (b'L', b'section L'), (b'M', b'section M'), (b'N', b'section N'), (b'SA', b'Ssection A'), (b'SB', b'Ssection B')])),
                ('student_gender', models.CharField(blank=True, max_length=2, null=True, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('student_address', models.CharField(max_length=100)),
            ],
        ),
    ]
