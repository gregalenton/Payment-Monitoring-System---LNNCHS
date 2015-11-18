# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disbursement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('disbursement_cost', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Due',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('due_name', models.CharField(max_length=45)),
                ('due_cost', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_name', models.CharField(max_length=50)),
                ('project_receiver', models.CharField(max_length=100)),
                ('project_cost', models.FloatField(default=0.0)),
            ],
        ),
        migrations.AddField(
            model_name='disbursement',
            name='disbursement_project',
            field=models.ForeignKey(to='funds.Project'),
        ),
    ]
