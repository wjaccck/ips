# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20161125_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='item_list',
            name='upstream',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='item_name',
            name='content',
            field=models.CharField(max_length=50, db_index=True),
        ),
        migrations.AlterField(
            model_name='item_name',
            name='dev_owner',
            field=models.CharField(db_index=True, max_length=200, null=True, blank=True),
        ),
    ]
