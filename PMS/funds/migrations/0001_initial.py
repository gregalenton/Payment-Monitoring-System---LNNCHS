# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disbursement',
            fields=[
                ('disbursement_id', models.AutoField(serialize=False, primary_key=True)),
                ('disbursement_cost', models.FloatField(default=0.0)),
            ],
        ),
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
                ('due_id', models.ForeignKey(to='funds.Due')),
                ('student_id', models.ForeignKey(to='accounts.StudentInfo')),
            ],
        ),
        migrations.AddField(
            model_name='disbursement',
            name='project_id',
            field=models.ForeignKey(to='funds.Project'),
        ),
    ]
