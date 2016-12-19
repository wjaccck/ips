# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_mysql_slaveof'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kafka',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('port', models.CharField(default='0', max_length=50)),
                ('detail', models.TextField(blank=True)),
                ('host', models.ForeignKey(related_name='kafka_link', to='api.Ipv4Address')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Zookeeper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('port', models.CharField(default='0', max_length=50)),
                ('detail', models.TextField(blank=True)),
                ('host', models.ForeignKey(related_name='zoo_link', to='api.Ipv4Address')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='codis',
            name='slaveof',
            field=models.ManyToManyField(related_name='codis_slave', to='api.Ipv4Address', blank=True),
        ),
        migrations.AddField(
            model_name='redis',
            name='slaveof',
            field=models.ManyToManyField(related_name='redis_slave', to='api.Ipv4Address', blank=True),
        ),
        migrations.AddField(
            model_name='sentinel',
            name='slaveof',
            field=models.ManyToManyField(related_name='sentinel_slave', to='api.Ipv4Address', blank=True),
        ),
        migrations.AlterField(
            model_name='mysql',
            name='slaveof',
            field=models.ManyToManyField(related_name='mysql_slave', to='api.Ipv4Address', blank=True),
        ),
        migrations.AddField(
            model_name='item_list',
            name='kafka',
            field=models.ManyToManyField(related_name='kafka', to='api.Kafka', blank=True),
        ),
        migrations.AddField(
            model_name='item_list',
            name='zookeeper',
            field=models.ManyToManyField(related_name='zookeeper', to='api.Zookeeper', blank=True),
        ),
    ]
