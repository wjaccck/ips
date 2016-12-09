# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20161118_1817'),
    ]

    operations = [
        migrations.CreateModel(
            name='Redis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('port', models.CharField(default='0', max_length=50)),
                ('detail', models.TextField(blank=True)),
                ('host', models.ForeignKey(related_name='redis_link', to='api.Ipv4Address')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='item_list',
            name='redis_link',
            field=models.ManyToManyField(related_name='redis', to='api.Mysql', blank=True),
        ),
    ]
