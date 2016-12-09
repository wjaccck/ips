# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_check_type_item_check'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item_check',
            name='content',
            field=models.CharField(max_length=250, blank=True),
        ),
        migrations.AlterField(
            model_name='item_check',
            name='headers',
            field=models.CharField(max_length=250, blank=True),
        ),
        migrations.AlterField(
            model_name='item_check',
            name='result',
            field=models.CharField(max_length=250, blank=True),
        ),
        migrations.AlterField(
            model_name='item_check',
            name='retcode',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
