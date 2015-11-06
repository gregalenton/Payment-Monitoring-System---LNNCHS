# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=16)),
                ('email_add', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Disbursement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('disbursement_id', models.IntegerField(default=0)),
                ('total_cost', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Due',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('due_id', models.IntegerField(default=0)),
                ('due_name', models.CharField(max_length=45)),
                ('cost', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Guardian',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('guardian_name', models.CharField(max_length=100)),
                ('guardian_address', models.CharField(max_length=100)),
                ('guardian_contact', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_number', models.IntegerField(default=0)),
                ('project_name', models.CharField(max_length=50)),
                ('receiver', models.CharField(max_length=100)),
                ('cost', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('receipt_no', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now=True)),
                ('due', models.ForeignKey(to='Database.Due')),
            ],
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('scholarship_id', models.IntegerField(default=0)),
                ('scholarship_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sibling',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sibling_name', models.CharField(max_length=100)),
                ('band_member', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=32)),
                ('student_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='receipt',
            name='student',
            field=models.ForeignKey(to='Database.Student'),
        ),
        migrations.AddField(
            model_name='disbursement',
            name='project',
            field=models.ForeignKey(to='Database.Project'),
        ),
    ]
