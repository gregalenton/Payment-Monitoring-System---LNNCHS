# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disbursement',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('cost', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Due',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=45)),
                ('cost', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('receiver', models.CharField(max_length=100)),
                ('cost', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('payment', models.IntegerField(default=0)),
                ('student_id', models.ForeignKey(to='accounts.Student')),
            ],
        ),
        migrations.AddField(
            model_name='disbursement',
            name='project',
            field=models.ForeignKey(to='funds.Project'),
        ),
    ]
