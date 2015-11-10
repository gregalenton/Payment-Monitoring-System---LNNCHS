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
                ('student_id', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('lastname', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=50)),
                ('middlename', models.CharField(max_length=50)),
                ('birthday', models.DateField(null=True, blank=True)),
                ('gender', models.CharField(blank=True, max_length=2, null=True, choices=[(b'M', b'Male'), (b'F', b'Female')])),
            ],
        ),
    ]
