# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20161213_1740'),
    ]

    operations = [
        migrations.CreateModel(
            name='RocketMQ',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('port', models.CharField(default='0', max_length=50)),
                ('detail', models.TextField(blank=True)),
                ('host', models.ForeignKey(related_name='mq_link', to='api.Ipv4Address')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='item_list',
            name='mq',
            field=models.ManyToManyField(related_name='mq', to='api.RocketMQ', blank=True),
        ),
    ]
