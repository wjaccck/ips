# encoding: utf8

from django.db.models import Count
from rest_framework import serializers
from netaddr import *
from abstract.serializers import CommonHyperlinkedModelSerializer
from .models import Ipv4Address, Ipv4Network,Machine,Site,Nginx,Type_name,Tech\
    ,Mysql,Application,Codis,Sentinel,Memcached,Es,Mcq,Tfs,Item_name,Item_list,Redis


class MachineSerializer(serializers.HyperlinkedModelSerializer):
    ips=serializers.SlugRelatedField(queryset=Ipv4Address.objects.all(), many=True,slug_field='name')
    class Meta:
        model = Machine

class Siteserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Site

class Type_nameserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type_name

class Nginxserializers(serializers.HyperlinkedModelSerializer):
    app_name=serializers.SlugRelatedField(queryset=Site.objects.all(), many=True,slug_field='content')
    host=serializers.SlugRelatedField(queryset=Ipv4Address.objects.all(),slug_field='name')
    type=serializers.SlugRelatedField(queryset=Type_name.objects.all(),slug_field='content')

    class Meta:
        model = Nginx



class IPv4AddressSerializer(CommonHyperlinkedModelSerializer):

    class Meta:
        model = Ipv4Address

class IPv4NetworkSerializer(CommonHyperlinkedModelSerializer): 


    class Meta:
        model = Ipv4Network

    def create(self, validated_data):
        prefix = validated_data['name']
        nwk = IPNetwork(prefix)        
        rawAddrs = [Ipv4Address(name=str(x), creator=validated_data['creator'], \
                    last_modified_by=validated_data['last_modified_by']) for x in list(nwk)]
        addresses = Ipv4Address.objects.bulk_create(rawAddrs, batch_size=30)
        return super(IPv4NetworkSerializer, self).create(validated_data)

    def validate(self, attrs):
        if attrs['name'].find('/') == -1:
            raise serializers.ValidationError('Network mask is missing!')

        return super(IPv4NetworkSerializer, self).validate(attrs)


class Techserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tech

class Mysqlserializers(serializers.HyperlinkedModelSerializer):
    host=serializers.SlugRelatedField(queryset=Ipv4Address.objects.all(),slug_field='name')
    class Meta:
        model = Mysql

class Applicationserializers(serializers.HyperlinkedModelSerializer):
    host=serializers.SlugRelatedField(queryset=Ipv4Address.objects.all(),slug_field='name')

    class Meta:
        model = Application

class Redisserializers(serializers.HyperlinkedModelSerializer):
    host=serializers.SlugRelatedField(queryset=Ipv4Address.objects.all(),slug_field='name')
    class Meta:
        model = Redis

class Codisserializers(serializers.HyperlinkedModelSerializer):
    host=serializers.SlugRelatedField(queryset=Ipv4Address.objects.all(),slug_field='name')
    class Meta:
        model = Codis

class Sentinelserializers(serializers.HyperlinkedModelSerializer):
    host=serializers.SlugRelatedField(queryset=Ipv4Address.objects.all(),slug_field='name')
    class Meta:
        model = Sentinel

class Memcachedserializers(serializers.HyperlinkedModelSerializer):
    host=serializers.SlugRelatedField(queryset=Ipv4Address.objects.all(),slug_field='name')
    class Meta:
        model = Memcached

class Esserializers(serializers.HyperlinkedModelSerializer):
    host=serializers.SlugRelatedField(queryset=Ipv4Address.objects.all(),slug_field='name')
    class Meta:
        model = Es

class Mcqserializers(serializers.HyperlinkedModelSerializer):
    host=serializers.SlugRelatedField(queryset=Ipv4Address.objects.all(),slug_field='name')
    class Meta:
        model = Mcq

class Tfsserializers(serializers.HyperlinkedModelSerializer):
    host=serializers.SlugRelatedField(queryset=Ipv4Address.objects.all(),slug_field='name')
    class Meta:
        model = Tfs

class Item_nameserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item_name

class Item_listserializers(serializers.ModelSerializer):
    item = serializers.StringRelatedField()
    app = serializers.StringRelatedField()
    tech = serializers.StringRelatedField()
    front = serializers.StringRelatedField(many=True)
    app_link = serializers.StringRelatedField(many=True)
    mysql_link = serializers.StringRelatedField(many=True)
    redis_link = serializers.StringRelatedField(many=True)
    codis_link = serializers.StringRelatedField(many=True)
    sentinel = serializers.StringRelatedField(many=True)
    memcache = serializers.StringRelatedField(many=True)
    es = serializers.StringRelatedField(many=True)
    mcq = serializers.StringRelatedField(many=True)
    tfs = serializers.StringRelatedField(many=True)
    dev_owner = serializers.SerializerMethodField(read_only=True)
    deploy_dir= serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Item_list


    def get_dev_owner(self, obj):
        return obj.item.dev_owner

    def get_deploy_dir(self, obj):
        return obj.item.location

