# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20161213_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item_list',
            name='item',
            field=models.ForeignKey(related_name='item_link', to='api.Item_name'),
        ),
    ]
