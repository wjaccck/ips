# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20161222_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='disk_info',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
