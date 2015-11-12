# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_student_student_scholarship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_scholarship',
            field=models.ForeignKey(blank=True, to='database.Scholarship', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_sibling',
            field=models.ManyToManyField(related_name='_student_sibling_+', null=True, to='database.Student', blank=True),
        ),
    ]
