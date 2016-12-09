# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_machine_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item_list',
            name='app',
            field=models.ForeignKey(related_name='site', blank=True, to='api.Site', null=True),
        ),
        migrations.AlterField(
            model_name='item_list',
            name='app_link',
            field=models.ManyToManyField(related_name='app', to='api.Application', blank=True),
        ),
        migrations.AlterField(
            model_name='item_list',
            name='codis_link',
            field=models.ManyToManyField(related_name='codis', to='api.Codis', blank=True),
        ),
        migrations.AlterField(
            model_name='item_list',
            name='es',
            field=models.ManyToManyField(related_name='es', to='api.Es', blank=True),
        ),
        migrations.AlterField(
            model_name='item_list',
            name='front',
            field=models.ManyToManyField(related_name='front', to='api.Ipv4Address', blank=True),
        ),
        migrations.AlterField(
            model_name='item_list',
            name='mcq',
            field=models.ManyToManyField(related_name='mcq', to='api.Mcq', blank=True),
        ),
        migrations.AlterField(
            model_name='item_list',
            name='memcache',
            field=models.ManyToManyField(related_name='memcache', to='api.Memcached', blank=True),
        ),
        migrations.AlterField(
            model_name='item_list',
            name='mysql_link',
            field=models.ManyToManyField(related_name='mysql', to='api.Mysql', blank=True),
        ),
        migrations.AlterField(
            model_name='item_list',
            name='sentinel',
            field=models.ManyToManyField(related_name='sentinel', to='api.Sentinel', blank=True),
        ),
        migrations.AlterField(
            model_name='item_list',
            name='tech',
            field=models.ForeignKey(related_name='tech', to='api.Tech'),
        ),
        migrations.AlterField(
            model_name='item_list',
            name='tfs',
            field=models.ManyToManyField(related_name='tfs', to='api.Tfs', blank=True),
        ),
    ]
