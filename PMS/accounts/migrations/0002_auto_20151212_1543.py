# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.IntegerField(choices=[(7, b'Grade 7'), (8, b'Grade 8'), (9, b'Grade 9'), (0, b'Grade 10'), (1, b'Grade 11'), (2, b'Grade 12')]),
        ),
    ]
