# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20161207_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='mysql',
            name='slaveof',
            field=models.ManyToManyField(related_name='mysql_slave', to='api.Ipv4Address'),
        ),
    ]
