# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Due',
            fields=[
                ('due_id', models.AutoField(serialize=False, primary_key=True)),
                ('due_name', models.CharField(max_length=45)),
                ('due_cost', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(serialize=False, primary_key=True)),
                ('project_name', models.CharField(max_length=50)),
                ('project_receiver', models.CharField(max_length=100)),
                ('project_cost', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('receipt_id', models.AutoField(serialize=False, primary_key=True)),
                ('receipt_timestamp', models.DateTimeField(auto_now_add=True)),
                ('amount', models.FloatField(default=0.0)),
                ('student_id', models.ForeignKey(to='accounts.StudentInfo')),
            ],
        ),
    ]
