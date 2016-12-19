# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20161214_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item_list',
            name='item',
            field=models.ForeignKey(to='api.Item_name'),
        ),
    ]
