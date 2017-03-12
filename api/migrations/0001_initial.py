# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('port', models.CharField(default='0', max_length=50)),
                ('detail', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
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
            name='Codis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('port', models.CharField(default='0', max_length=50)),
                ('detail', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Docker_list',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, blank=True)),
                ('docker_id', models.CharField(max_length=200, db_index=True)),
                ('ports', models.CharField(max_length=200, blank=True)),
                ('status', models.CharField(default='unknown', max_length=50, db_index=True)),
                ('app', models.CharField(max_length=200)),
                ('version', models.CharField(max_length=200)),
                ('remark', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Es',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('port', models.CharField(default='0', max_length=50)),
                ('detail', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ipv4Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=80)),
                ('description', models.CharField(max_length=255, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(related_name='api_ipv4address_creator', verbose_name=b'creator', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(related_name='api_ipv4address_last_modified_by', verbose_name=b'last modified by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Ipv4Network',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=80)),
                ('description', models.CharField(max_length=255, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('gateway', models.CharField(max_length=18, null=True)),
                ('creator', models.ForeignKey(related_name='api_ipv4network_creator', verbose_name=b'creator', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(related_name='api_ipv4network_last_modified_by', verbose_name=b'last modified by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
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
                ('headers', models.CharField(max_length=250, blank=True)),
                ('port', models.IntegerField()),
                ('content', models.CharField(max_length=250, blank=True)),
                ('link_address', models.CharField(max_length=250)),
                ('retcode', models.CharField(max_length=50, blank=True)),
                ('result', models.CharField(max_length=250, blank=True)),
                ('remark', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Item_list',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('upstream', models.CharField(max_length=200, blank=True)),
                ('app_location', models.CharField(max_length=200, null=True, blank=True)),
                ('remark', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Item_name',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('content', models.CharField(max_length=50, db_index=True)),
                ('module', models.CharField(max_length=50, null=True, blank=True)),
                ('alias', models.CharField(max_length=50, null=True, blank=True)),
                ('dev_owner', models.CharField(db_index=True, max_length=200, null=True, blank=True)),
                ('ops_owner', models.CharField(max_length=200, null=True, blank=True)),
                ('test_owner', models.CharField(max_length=200, null=True, blank=True)),
                ('location', models.CharField(max_length=250, null=True, blank=True)),
                ('git_url', models.CharField(max_length=200, null=True, blank=True)),
                ('remark', models.TextField(max_length=250, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
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
            name='Machine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('memory', models.IntegerField(blank=True)),
                ('cpu', models.IntegerField(blank=True)),
                ('disk_info', models.CharField(max_length=200, blank=True)),
                ('product', models.CharField(max_length=100, verbose_name='\u670d\u52a1\u5668\u7c7b\u578b')),
                ('machine_id', models.CharField(max_length=200, null=True, blank=True)),
                ('serial', models.CharField(max_length=200, null=True, blank=True)),
                ('system_id', models.CharField(max_length=50)),
                ('sys_desc', models.CharField(max_length=50)),
                ('major_release', models.CharField(max_length=50)),
                ('idc', models.CharField(default='hz', max_length=50)),
                ('company', models.CharField(max_length=50, blank=True)),
                ('ips', models.ManyToManyField(to='api.Ipv4Address')),
                ('mark', models.ForeignKey(related_name='mark', blank=True, to='api.Ipv4Address', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mcq',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('port', models.CharField(default='0', max_length=50)),
                ('detail', models.TextField(blank=True)),
                ('host', models.ForeignKey(related_name='mcq_link', to='api.Ipv4Address')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Memcached',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('port', models.CharField(default='0', max_length=50)),
                ('detail', models.TextField(blank=True)),
                ('host', models.ForeignKey(related_name='memcache_link', to='api.Ipv4Address')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mysql',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('port', models.CharField(default='0', max_length=50)),
                ('detail', models.TextField(blank=True)),
                ('name', models.CharField(max_length=50)),
                ('host', models.ForeignKey(related_name='mysql_link', to='api.Ipv4Address')),
                ('slaveof', models.ManyToManyField(related_name='mysql_slave', to='api.Ipv4Address', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Nginx',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('file_name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ops_act_history',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50, verbose_name='\u7c7b\u522b')),
                ('operator', models.CharField(max_length=50)),
                ('content', models.TextField(verbose_name='\u5185\u5bb9')),
                ('creator', models.ForeignKey(related_name='api_ops_act_history_creator', verbose_name='creator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Ops_plan_history',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50, verbose_name='\u7c7b\u522b')),
                ('operator', models.CharField(max_length=50)),
                ('content', models.TextField(verbose_name='\u5185\u5bb9')),
                ('status', models.CharField(max_length=50)),
                ('creator', models.ForeignKey(related_name='api_ops_plan_history_creator', verbose_name='creator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Redis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('port', models.CharField(default='0', max_length=50)),
                ('detail', models.TextField(blank=True)),
                ('host', models.ForeignKey(related_name='redis_link', to='api.Ipv4Address')),
                ('slaveof', models.ManyToManyField(related_name='redis_slave', to='api.Ipv4Address', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
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
        migrations.CreateModel(
            name='Sentinel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('port', models.CharField(default='0', max_length=50)),
                ('detail', models.TextField(blank=True)),
                ('host', models.ForeignKey(related_name='sentinel_link', to='api.Ipv4Address')),
                ('slaveof', models.ManyToManyField(related_name='sentinel_slave', to='api.Ipv4Address', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Site',
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
            name='Tech',
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
            name='Tfs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('port', models.CharField(default='0', max_length=50)),
                ('detail', models.TextField(blank=True)),
                ('host', models.ForeignKey(related_name='tfs_link', to='api.Ipv4Address')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Type_name',
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
            name='Version_history',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('project', models.CharField(default='shihui', max_length=50)),
                ('environment', models.CharField(max_length=50)),
                ('version', models.CharField(max_length=50)),
                ('build', models.CharField(max_length=50)),
                ('file_name', models.CharField(max_length=200, blank=True)),
                ('file_url', models.URLField(blank=True)),
                ('config_name', models.CharField(max_length=200, blank=True)),
                ('config_url', models.URLField(blank=True)),
                ('latest_status', models.BooleanField(default=True)),
                ('module', models.ForeignKey(to='api.Item_name')),
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
            model_name='nginx',
            name='app_name',
            field=models.ManyToManyField(to='api.Site'),
        ),
        migrations.AddField(
            model_name='nginx',
            name='host',
            field=models.ForeignKey(related_name='nginx_link', to='api.Ipv4Address'),
        ),
        migrations.AddField(
            model_name='nginx',
            name='type',
            field=models.ForeignKey(to='api.Type_name'),
        ),
        migrations.AddField(
            model_name='item_list',
            name='app',
            field=models.ForeignKey(related_name='site', blank=True, to='api.Site', null=True),
        ),
        migrations.AddField(
            model_name='item_list',
            name='app_link',
            field=models.ManyToManyField(related_name='app', to='api.Application', blank=True),
        ),
        migrations.AddField(
            model_name='item_list',
            name='codis_link',
            field=models.ManyToManyField(related_name='codis', to='api.Codis', blank=True),
        ),
        migrations.AddField(
            model_name='item_list',
            name='es',
            field=models.ManyToManyField(related_name='es', to='api.Es', blank=True),
        ),
        migrations.AddField(
            model_name='item_list',
            name='front',
            field=models.ManyToManyField(related_name='front', to='api.Ipv4Address', blank=True),
        ),
        migrations.AddField(
            model_name='item_list',
            name='item',
            field=models.ForeignKey(to='api.Item_name'),
        ),
        migrations.AddField(
            model_name='item_list',
            name='kafka',
            field=models.ManyToManyField(related_name='kafka', to='api.Kafka', blank=True),
        ),
        migrations.AddField(
            model_name='item_list',
            name='mcq',
            field=models.ManyToManyField(related_name='mcq', to='api.Mcq', blank=True),
        ),
        migrations.AddField(
            model_name='item_list',
            name='memcache',
            field=models.ManyToManyField(related_name='memcache', to='api.Memcached', blank=True),
        ),
        migrations.AddField(
            model_name='item_list',
            name='mq',
            field=models.ManyToManyField(related_name='mq', to='api.RocketMQ', blank=True),
        ),
        migrations.AddField(
            model_name='item_list',
            name='mysql_link',
            field=models.ManyToManyField(related_name='mysql', to='api.Mysql', blank=True),
        ),
        migrations.AddField(
            model_name='item_list',
            name='redis_link',
            field=models.ManyToManyField(related_name='redis', to='api.Redis', blank=True),
        ),
        migrations.AddField(
            model_name='item_list',
            name='sentinel',
            field=models.ManyToManyField(related_name='sentinel', to='api.Sentinel', blank=True),
        ),
        migrations.AddField(
            model_name='item_list',
            name='tech',
            field=models.ForeignKey(related_name='tech', to='api.Tech'),
        ),
        migrations.AddField(
            model_name='item_list',
            name='tfs',
            field=models.ManyToManyField(related_name='tfs', to='api.Tfs', blank=True),
        ),
        migrations.AddField(
            model_name='item_list',
            name='zookeeper',
            field=models.ManyToManyField(related_name='zookeeper', to='api.Zookeeper', blank=True),
        ),
        migrations.AddField(
            model_name='item_check',
            name='item',
            field=models.ForeignKey(to='api.Item_name'),
        ),
        migrations.AddField(
            model_name='item_check',
            name='type',
            field=models.ForeignKey(to='api.Check_type'),
        ),
        migrations.AddField(
            model_name='es',
            name='host',
            field=models.ForeignKey(related_name='es_link', to='api.Ipv4Address'),
        ),
        migrations.AddField(
            model_name='docker_list',
            name='host',
            field=models.ForeignKey(to='api.Ipv4Address'),
        ),
        migrations.AddField(
            model_name='docker_list',
            name='item',
            field=models.ForeignKey(to='api.Item_name'),
        ),
        migrations.AddField(
            model_name='docker_list',
            name='tech',
            field=models.ForeignKey(blank=True, to='api.Tech', null=True),
        ),
        migrations.AddField(
            model_name='codis',
            name='host',
            field=models.ForeignKey(related_name='codis_link', to='api.Ipv4Address'),
        ),
        migrations.AddField(
            model_name='codis',
            name='slaveof',
            field=models.ManyToManyField(related_name='codis_slave', to='api.Ipv4Address', blank=True),
        ),
        migrations.AddField(
            model_name='application',
            name='host',
            field=models.ForeignKey(related_name='app_link', to='api.Ipv4Address'),
        ),
    ]
