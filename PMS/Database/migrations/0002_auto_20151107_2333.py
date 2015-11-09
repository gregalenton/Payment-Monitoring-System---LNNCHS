# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='admin_user',
            field=models.OneToOneField(related_name='admin', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_user',
            field=models.OneToOneField(related_name='student', to=settings.AUTH_USER_MODEL),
        ),
    ]
