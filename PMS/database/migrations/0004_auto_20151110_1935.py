# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_auto_20151110_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_sibling',
            field=models.ManyToManyField(related_name='_student_sibling_+', to='database.Student'),
        ),
    ]
