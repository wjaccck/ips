# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20161214_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('content', models.CharField(unique=True, max_length=50)),
                ('alias', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='machine',
            name='mark',
            field=models.ForeignKey(related_name='mark', blank=True, to='api.Ipv4Address', null=True),
        ),
    ]
