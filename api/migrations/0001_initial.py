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
            name='Item_list',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
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
                ('content', models.CharField(max_length=50)),
                ('module', models.CharField(max_length=50, null=True, blank=True)),
                ('alias', models.CharField(max_length=50, null=True, blank=True)),
                ('dev_owner', models.CharField(max_length=200, null=True, blank=True)),
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
            name='Kvm_list',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('idc', models.CharField(max_length=200)),
                ('zone', models.CharField(max_length=200)),
                ('item', models.ForeignKey(to='api.Item_name')),
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
                ('product', models.CharField(max_length=100, verbose_name='\u670d\u52a1\u5668\u7c7b\u578b')),
                ('machine_id', models.CharField(max_length=200, null=True, blank=True)),
                ('serial', models.CharField(max_length=200, null=True, blank=True)),
                ('system_id', models.CharField(max_length=50)),
                ('sys_desc', models.CharField(max_length=50)),
                ('major_release', models.CharField(max_length=50)),
                ('idc', models.CharField(default='hz', max_length=50)),
                ('ips', models.ManyToManyField(to='api.Ipv4Address')),
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
                ('host', models.ForeignKey(to='api.Ipv4Address')),
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
                ('host', models.ForeignKey(to='api.Ipv4Address')),
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
                ('host', models.ForeignKey(to='api.Ipv4Address')),
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
            name='Sentinel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('port', models.CharField(default='0', max_length=50)),
                ('detail', models.TextField(blank=True)),
                ('host', models.ForeignKey(to='api.Ipv4Address')),
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
                ('host', models.ForeignKey(to='api.Ipv4Address')),
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
        migrations.AddField(
            model_name='nginx',
            name='app_name',
            field=models.ManyToManyField(to='api.Site'),
        ),
        migrations.AddField(
            model_name='nginx',
            name='host',
            field=models.ForeignKey(to='api.Ipv4Address'),
        ),
        migrations.AddField(
            model_name='nginx',
            name='type',
            field=models.ForeignKey(to='api.Type_name'),
        ),
        migrations.AddField(
            model_name='item_list',
            name='app',
            field=models.ForeignKey(blank=True, to='api.Site', null=True),
        ),
        migrations.AddField(
            model_name='item_list',
            name='app_link',
            field=models.ManyToManyField(to='api.Application', blank=True),
        ),
        migrations.AddField(
            model_name='item_list',
            name='codis_link',
            field=models.ManyToManyField(to='api.Codis', blank=True),
        ),
        migrations.AddField(
            model_name='item_list',
            name='es',
            field=models.ManyToManyField(to='api.Es', blank=True),
        ),
        migrations.AddField(
            model_name='item_list',
            name='front',
            field=models.ManyToManyField(to='api.Ipv4Address', blank=True),
        ),
        migrations.AddField(
            model_name='item_list',
            name='item',
            field=models.ForeignKey(to='api.Item_name'),
        ),
        migrations.AddField(
            model_name='item_list',
            name='mcq',
            field=models.ManyToManyField(to='api.Mcq', blank=True),
        ),
        migrations.AddField(
            model_name='item_list',
            name='memcache',
            field=models.ManyToManyField(to='api.Memcached', blank=True),
        ),
        migrations.AddField(
            model_name='item_list',
            name='mysql_link',
            field=models.ManyToManyField(to='api.Mysql', blank=True),
        ),
        migrations.AddField(
            model_name='item_list',
            name='sentinel',
            field=models.ManyToManyField(to='api.Sentinel', blank=True),
        ),
        migrations.AddField(
            model_name='item_list',
            name='tech',
            field=models.ForeignKey(to='api.Tech'),
        ),
        migrations.AddField(
            model_name='item_list',
            name='tfs',
            field=models.ManyToManyField(to='api.Tfs', blank=True),
        ),
        migrations.AddField(
            model_name='es',
            name='host',
            field=models.ForeignKey(to='api.Ipv4Address'),
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
            field=models.ForeignKey(to='api.Ipv4Address'),
        ),
        migrations.AddField(
            model_name='application',
            name='host',
            field=models.ForeignKey(to='api.Ipv4Address'),
        ),
    ]
