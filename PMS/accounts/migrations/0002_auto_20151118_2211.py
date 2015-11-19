# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='student_year',
            field=models.CharField(blank=True, max_length=30, choices=[(b'7', b'grade 7'), (b'8', b'grade 8'), (b'9', b'grade 9'), (b'10', b'grade 10'), (b'11', b'grade 11'), (b'12', b'grade 12')]),
        ),
    ]
