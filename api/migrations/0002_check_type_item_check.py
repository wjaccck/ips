# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Check_type',
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
        migrations.CreateModel(
            name='Item_check',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, '\u6b63\u5e38'), (1, '\u5f02\u5e38')])),
                ('method', models.CharField(max_length=50, blank=True)),
                ('headers', models.CharField(max_length=250)),
                ('port', models.IntegerField()),
                ('content', models.CharField(max_length=250)),
                ('link_address', models.CharField(max_length=250)),
                ('retcode', models.CharField(max_length=50)),
                ('result', models.CharField(max_length=250)),
                ('remark', models.TextField(blank=True)),
                ('item', models.ForeignKey(to='api.Item_name')),
                ('type', models.ForeignKey(to='api.Check_type')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
