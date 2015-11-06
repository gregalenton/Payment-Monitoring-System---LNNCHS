# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('admin_num', models.IntegerField(default=0)),
                ('admin_user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
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
                ('project_name', models.CharField(max_length=50)),
                ('project_receiver', models.CharField(max_length=100)),
                ('project_cost', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('scholarship_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('student_year', models.IntegerField(choices=[(b'7', b'grade 7'), (b'8', b'grade 8'), (b'9', b'grade 9'), (b'10', b'grade 10'), (b'11', b'grade 11'), (b'12', b'grade 12')])),
                ('student_section', models.CharField(max_length=2, choices=[(b'A', b'section A'), (b'B', b'section B'), (b'C', b'section C'), (b'D', b'section D'), (b'E', b'section E'), (b'F', b'section F'), (b'G', b'section G'), (b'H', b'section H'), (b'I', b'section I'), (b'J', b'section J'), (b'K', b'section K'), (b'L', b'section L'), (b'M', b'section M'), (b'N', b'section N'), (b'SA', b'Ssection A'), (b'SB', b'Ssection B')])),
                ('student_address', models.CharField(max_length=100)),
                ('student_bandMem', models.BooleanField(default=False)),
                ('student_payed', models.FloatField(default=0.0)),
                ('student_toPay', models.FloatField(default=0.0)),
                ('student_guardian', models.ForeignKey(to='database.Guardian')),
                ('student_sibling', models.ManyToManyField(related_name='_student_sibling_+', to='database.Student')),
                ('student_user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='disbursement',
            name='disbursement_project',
            field=models.ForeignKey(to='database.Project'),
        ),
    ]
