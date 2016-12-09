# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20161117_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='company',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
