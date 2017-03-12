# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='version_history',
            name='config_md5',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='version_history',
            name='file_md5',
            field=models.URLField(blank=True),
        ),
    ]
