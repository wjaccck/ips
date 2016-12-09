# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20161125_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item_list',
            name='redis_link',
            field=models.ManyToManyField(related_name='redis', to='api.Redis', blank=True),
        ),
    ]
