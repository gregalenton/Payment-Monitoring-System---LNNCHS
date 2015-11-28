# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_sibling',
            field=models.ManyToManyField(related_name='student_sibling_rel_+', to='accounts.Student'),
        ),
    ]
