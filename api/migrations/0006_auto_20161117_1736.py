# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20161117_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='host',
            field=models.ForeignKey(related_name='app_link', to='api.Ipv4Address'),
        ),
        migrations.AlterField(
            model_name='codis',
            name='host',
            field=models.ForeignKey(related_name='codis_link', to='api.Ipv4Address'),
        ),
        migrations.AlterField(
            model_name='es',
            name='host',
            field=models.ForeignKey(related_name='es_link', to='api.Ipv4Address'),
        ),
        migrations.AlterField(
            model_name='mcq',
            name='host',
            field=models.ForeignKey(related_name='mcq_link', to='api.Ipv4Address'),
        ),
        migrations.AlterField(
            model_name='memcached',
            name='host',
            field=models.ForeignKey(related_name='memcache_link', to='api.Ipv4Address'),
        ),
        migrations.AlterField(
            model_name='mysql',
            name='host',
            field=models.ForeignKey(related_name='mysql_link', to='api.Ipv4Address'),
        ),
        migrations.AlterField(
            model_name='nginx',
            name='host',
            field=models.ForeignKey(related_name='nginx_link', to='api.Ipv4Address'),
        ),
        migrations.AlterField(
            model_name='sentinel',
            name='host',
            field=models.ForeignKey(related_name='sentinel_link', to='api.Ipv4Address'),
        ),
        migrations.AlterField(
            model_name='tfs',
            name='host',
            field=models.ForeignKey(related_name='tfs_link', to='api.Ipv4Address'),
        ),
    ]
