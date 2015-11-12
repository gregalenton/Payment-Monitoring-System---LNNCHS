# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Funds', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='funds',
            options={'verbose_name': 'Fund', 'verbose_name_plural': 'Funds'},
        ),
    ]
