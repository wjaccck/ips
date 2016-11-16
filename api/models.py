#coding=utf-8
from __future__ import unicode_literals

from django.db import models
from abstract.models import CommonModel,UniqueNameDescModel,API_BASE,APPLY_BASE,IDC_BASE,ITEM_BASE

# Create your models here.



class Ipv4Address(UniqueNameDescModel):

    class Meta:
        ordering = ['name', ]

class Ipv4Network(UniqueNameDescModel):
    gateway = models.CharField(max_length=18, null=True)

    class Meta:
        ordering = ['name', ]

class Machine(CommonModel,IDC_BASE):
    ips=models.ManyToManyField(Ipv4Address)
    name=models.CharField(max_length=100)
    memory=models.IntegerField(blank=True)
    cpu=models.IntegerField(blank=True)
    product=models.CharField(max_length=100,verbose_name=u'服务器类型')
    machine_id=models.CharField(max_length=200,blank=True,null=True)
    serial=models.CharField(max_length=200,blank=True,null=True)
    system_id=models.CharField(max_length=50)
    sys_desc=models.CharField(max_length=50)
    major_release=models.CharField(max_length=50)
    idc=models.CharField(max_length=50,default='hz')
    def __unicode__(self):
        return self.name

    @staticmethod
    def verbose():
        return u'服务器信息'

### nginx info
class Site(CommonModel,API_BASE):
    content=models.CharField(max_length=50,unique=True)
    alias=models.CharField(max_length=50,unique=True)
    def __unicode__(self):
        return self.content

    @staticmethod
    def verbose():
        return u'站点'

class Type_name(CommonModel,API_BASE):
    content=models.CharField(max_length=50,unique=True)
    alias=models.CharField(max_length=50,unique=True)
    def __unicode__(self):
        return self.content
    @staticmethod
    def verbose():
        return u'前端类型'

class Nginx(CommonModel,ITEM_BASE):
    host=models.ForeignKey(Ipv4Address)
    type=models.ForeignKey(Type_name)
    app_name=models.ManyToManyField(Site)
    file_name=models.CharField(max_length=200)
    @staticmethod
    def verbose():
        return u'nginx详情'
### app info
class Link_info(CommonModel):
    host=models.ForeignKey(Ipv4Address)
    port=models.CharField(max_length=50,default='0')
    detail=models.TextField(blank=True)
    def __unicode__(self):
        return "%s:%s" %(self.host.name,self.port)
    class Meta:
        abstract = True
########

class Tech(CommonModel,API_BASE):
    content=models.CharField(max_length=50,unique=True)
    alias=models.CharField(max_length=50,unique=True)
    def __unicode__(self):
        return self.content

    @staticmethod
    def verbose():
        return u'技术栈'

class Mysql(Link_info,API_BASE):
    name=models.CharField(max_length=50)
    def __unicode__(self):
        return "%s:%s/%s" %(self.host.name,self.port,self.name)

    @staticmethod
    def verbose():
        return u'数据库'

class Application(Link_info,API_BASE):
    def __unicode__(self):
        return "%s:%s/%s" %(self.host.name,self.port,self.detail)

    @staticmethod
    def verbose():
        return u'应用信息'

class Codis(Link_info,API_BASE):
    pass
    @staticmethod
    def verbose():
        return u'Codis'

class Sentinel(Link_info,API_BASE):
    pass

    @staticmethod
    def verbose():
        return u'Sentinel'

class Memcached(Link_info,API_BASE):
    pass
    @staticmethod
    def verbose():
        return u'MC'

class Es(Link_info,API_BASE):
    pass
    @staticmethod
    def verbose():
        return u'ES'

class Mcq(Link_info,API_BASE):
    pass
    @staticmethod
    def verbose():
        return u'MCQ'

class Tfs(Link_info,API_BASE):
    pass
    @staticmethod
    def verbose():
        return u'TFS'
class Item_name(CommonModel,API_BASE):
    content=models.CharField(max_length=50)
    module=models.CharField(max_length=50,blank=True,null=True)
    alias=models.CharField(max_length=50,blank=True,null=True)
    dev_owner=models.CharField(max_length=200,blank=True,null=True)
    ops_owner=models.CharField(max_length=200,blank=True,null=True)
    test_owner=models.CharField(max_length=200,blank=True,null=True)
    location=models.CharField(max_length=250,blank=True,null=True)
    git_url=models.CharField(max_length=200,blank=True,null=True)
    remark=models.TextField(max_length=250,blank=True,null=True)
    def __unicode__(self):
        return "%s-%s" %(self.content,self.module)

    @staticmethod
    def verbose():
        return u'项目列表'


class Item_list(CommonModel,ITEM_BASE):
    item=models.ForeignKey(Item_name)
    app=models.ForeignKey(Site,blank=True,null=True)
    tech=models.ForeignKey(Tech)
    front=models.ManyToManyField(Ipv4Address,blank=True)
    app_link=models.ManyToManyField(Application,blank=True)
    mysql_link=models.ManyToManyField(Mysql,blank=True)
    codis_link=models.ManyToManyField(Codis,blank=True)
    sentinel=models.ManyToManyField(Sentinel,blank=True)
    memcache=models.ManyToManyField(Memcached,blank=True)
    es=models.ManyToManyField(Es,blank=True)
    mcq=models.ManyToManyField(Mcq,blank=True)
    tfs=models.ManyToManyField(Tfs,blank=True)
    app_location=models.CharField(max_length=200,blank=True,null=True)
    remark=models.TextField(blank=True)

    @staticmethod
    def verbose():
        return u'项目部署详情'

class Kvm_list(CommonModel,APPLY_BASE):
    idc=models.CharField(max_length=200)
    zone=models.CharField(max_length=200)
    item=models.ForeignKey(Item_name)
    @staticmethod
    def verbose():
        return u'KVM'
class Docker_list(CommonModel,APPLY_BASE):
    host=models.ForeignKey(Ipv4Address)
    name=models.CharField(max_length=200,blank= True)
    docker_id=models.CharField(max_length=200,db_index=True)
    ports=models.CharField(max_length=200,blank=True)
    tech=models.ForeignKey(Tech,blank=True,null=True)
    status=models.CharField(max_length=50,db_index=True,default='unknown')
    item=models.ForeignKey(Item_name)
    app=models.CharField(max_length=200)
    version=models.CharField(max_length=200)
    remark=models.TextField(blank=True,null=True)

    @staticmethod
    def verbose():
        return u'DOCKER'