#coding=utf-8
from __future__ import unicode_literals

from django.db import models
from abstract.models import CommonModel,UniqueNameDescModel,API_BASE,APPLY_BASE,IDC_BASE,ITEM_BASE,HISTORY_BASE,PUBLISH_BASE
# Create your models here.



class Ipv4Address(UniqueNameDescModel):

    class Meta:
        ordering = ['name', ]

class Ipv4Network(UniqueNameDescModel):
    gateway = models.CharField(max_length=18, null=True)

    class Meta:
        ordering = ['name', ]

class Machine(CommonModel,IDC_BASE):
    console_ip=models.OneToOneField(Ipv4Address,related_name='console_ip')
    ipv4=models.ManyToManyField(Ipv4Address,blank=True)
    cpu=models.CharField(max_length=100,blank=True)
    kernel=models.CharField(max_length=100,blank=True)
    cpu_number=models.IntegerField(blank=True)
    vcpu_number=models.IntegerField(blank=True)
    cpu_core=models.IntegerField(blank=True)
    hostname=models.CharField(max_length=100,blank=True)
    memory=models.IntegerField(blank=True)
    disk=models.CharField(max_length=100,blank=True)
    swap=models.CharField(max_length=100,blank=True)
    product = models.CharField(max_length=100, verbose_name=u'服务器类型', blank=True)
    selinux = models.CharField(max_length=10, blank=True)
    distribution=models.CharField(max_length=25, blank=True)
    distribution_version=models.CharField(max_length=25,blank=True)
    manufacturer=models.CharField(max_length=25, blank=True)
    serial = models.CharField(max_length=10, blank=True)
    status=models.IntegerField(blank=True)

    idc=models.CharField(max_length=50,blank=True)
    company=models.CharField(max_length=50,blank=True)
    def __unicode__(self):
        return self.console_ip.name

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

class Resource_type(CommonModel,API_BASE):
    content=models.CharField(max_length=50,unique=True)
    alias=models.CharField(max_length=50,unique=True)
    def __unicode__(self):
        return self.content
    @staticmethod
    def verbose():
        return u'资源类型'


class Nginx(CommonModel,ITEM_BASE):
    host=models.ForeignKey(Ipv4Address,related_name='nginx_link')
    type=models.ForeignKey(Type_name)
    app_name=models.ManyToManyField(Site)
    file_name=models.CharField(max_length=200)
    @staticmethod
    def verbose():
        return u'nginx详情'
### app info
class Link_info(CommonModel):
    # host=models.ForeignKey(Ipv4Address)
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
    host=models.ForeignKey(Ipv4Address,related_name='mysql_link')
    slaveof=models.ManyToManyField(Ipv4Address,blank=True,related_name='mysql_slave')
    # proxy_host=models.ForeignKey(Ipv4Address,blank=True,default='',related_name='proxy_host')
    # proxy_port=models.CharField(max_length=50,blank=True)
    def __unicode__(self):
        # if self.proxy_host:
        return "%s:%s/%s" %(self.host.name,self.port,self.name)
        # else:
        #     return "%s:%s/%s" %(self.proxy_host.name,self.proxy_port,self.name)

    @staticmethod
    def verbose():
        return u'数据库'

# class Mysql_Cluster(CommonModel,API_BASE):
#     master=models.ForeignKey(Mysql)
#     slave=models.ManyToManyField(Mysql,blank=True)
#     def __unicode__(self):
#         return self.master
#
#     @staticmethod
#     def verbose():
#         return u'数据库集群'

class Zookeeper(Link_info,API_BASE):
    host=models.ForeignKey(Ipv4Address,related_name='zoo_link')
    def __unicode__(self):
        return "%s:%s" %(self.host.name,self.port)

    @staticmethod
    def verbose():
        return u'zookeeper'

class Kafka(Link_info,API_BASE):
    host=models.ForeignKey(Ipv4Address,related_name='kafka_link')
    def __unicode__(self):
        return "%s:%s" %(self.host.name,self.port)

    @staticmethod
    def verbose():
        return u'kafka'

class RocketMQ(Link_info,API_BASE):
    host=models.ForeignKey(Ipv4Address,related_name='mq_link')
    def __unicode__(self):
        return "%s:%s" %(self.host.name,self.port)

    @staticmethod
    def verbose():
        return u'mq'

class Application(Link_info,API_BASE):
    host=models.ForeignKey(Ipv4Address,related_name='app_link')
    def __unicode__(self):
        return "%s:%s/%s" %(self.host.name,self.port,self.detail)

    @staticmethod
    def verbose():
        return u'应用信息'



class Redis(Link_info,API_BASE):
    host=models.ForeignKey(Ipv4Address,related_name='redis_link')
    slaveof=models.ManyToManyField(Ipv4Address,blank=True,related_name='redis_slave')
    @staticmethod
    def verbose():
        return u'Redis'

class Codis(Link_info,API_BASE):
    host=models.ForeignKey(Ipv4Address,related_name='codis_link')
    slaveof=models.ManyToManyField(Ipv4Address,blank=True,related_name='codis_slave')
    @staticmethod
    def verbose():
        return u'Codis'

class Sentinel(Link_info,API_BASE):
    host=models.ForeignKey(Ipv4Address,related_name='sentinel_link')
    slaveof=models.ManyToManyField(Ipv4Address,blank=True,related_name='sentinel_slave')
    @staticmethod
    def verbose():
        return u'Sentinel'

# class App_Resource(API_BASE):
#     host=models.ForeignKey(Ipv4Address,related_name='')
#     resource_type=models.ForeignKey(Resource_type)
#     machine=models.ForeignKey(Machine,related_name='machine')
#     cpu=models.IntegerField(blank=True)
#     memory=models.IntegerField(blank=True,verbose_name='单位为G')
#     disk=models.IntegerField(blank=True,verbose_name='单位为G')
#     belongto=models.CharField(max_length=25)
#     @staticmethod
#     def verbose():
#         return u'resource'

#
# class Resource(API_BASE):
#     machine=models.ForeignKey(Machine,related_name='machine')
#     mark=models.ForeignKey(Ipv4Address,related_name='mark')
#     cpu=models.IntegerField(blank=True)
#     memory=models.IntegerField(blank=True,verbose_name='单位为G')
#     disk=models.IntegerField(blank=True,verbose_name='单位为G')
#     ipaddresses=models.ManyToManyField(Ipv4Address)
#     belongto=models.CharField(max_length=25)
#     @staticmethod
#     def verbose():
#         return u'resource'

class Memcached(Link_info,API_BASE):
    host=models.ForeignKey(Ipv4Address,related_name='memcache_link')
    @staticmethod
    def verbose():
        return u'MC'

class Es(Link_info,API_BASE):
    host=models.ForeignKey(Ipv4Address,related_name='es_link')
    @staticmethod
    def verbose():
        return u'ES'

class Mcq(Link_info,API_BASE):
    host=models.ForeignKey(Ipv4Address,related_name='mcq_link')
    @staticmethod
    def verbose():
        return u'MCQ'

class Tfs(Link_info,API_BASE):
    host=models.ForeignKey(Ipv4Address,related_name='tfs_link')
    @staticmethod
    def verbose():
        return u'TFS'

class Item_name(CommonModel,API_BASE):
    content=models.CharField(max_length=50,db_index=True)
    module=models.CharField(max_length=50,blank=True,null=True)
    alias=models.CharField(max_length=50,blank=True,null=True)
    dev_owner=models.CharField(max_length=200,blank=True,null=True,db_index=True)
    ops_owner=models.CharField(max_length=200,blank=True,null=True)
    test_owner=models.CharField(max_length=200,blank=True,null=True)
    location=models.CharField(max_length=250,blank=True,null=True)
    git_url=models.CharField(max_length=200,blank=True,null=True)
    remark=models.TextField(max_length=250,blank=True,null=True)
    def __unicode__(self):
        if self.module:
            return "%s:%s" %(self.content,self.module)
        else:
            return self.module

    @staticmethod
    def verbose():
        return u'项目列表'

class Version_history(CommonModel,APPLY_BASE):
    project=models.CharField(max_length=50,default='shihui')
    module=models.ForeignKey(Item_name)
    environment=models.CharField(max_length=50)
    version=models.CharField(max_length=50)
    build=models.CharField(max_length=50)
    file_name=models.CharField(max_length=200,blank=True)
    file_url=models.URLField(blank=True)
    file_md5=models.URLField(blank=True)
    config_name=models.CharField(max_length=200,blank=True)
    config_url=models.URLField(blank=True)
    config_md5=models.URLField(blank=True)
    latest_status=models.BooleanField(default=True)

    def __unicode__(self):
        return "%s:%s" %(self.module.content,self.version)

    @staticmethod
    def verbose():
        return u'构建历史'

    def save(self, *args, **kwargs):
        Version_history.objects.filter(module=self.module).update(latest_status=False)
        return super(Version_history, self).save(*args, **kwargs)


class Ops_act_history(CommonModel,HISTORY_BASE):
    title=models.CharField(max_length=50,verbose_name=u'类别')
    operator=models.CharField(max_length=50,)
    content=models.TextField(verbose_name=u'内容')
    creator = models.ForeignKey('auth.user', related_name='%(app_label)s_%(class)s_creator', verbose_name='creator')

    @staticmethod
    def verbose():
        return u'线上操作历史'
    class Meta:
        ordering=['-created_date']


class Ops_plan_history(CommonModel,HISTORY_BASE):
    title=models.CharField(max_length=50,verbose_name=u'类别')
    operator=models.CharField(max_length=50,)
    content=models.TextField(verbose_name=u'内容')
    status=models.CharField(max_length=50)
    creator = models.ForeignKey('auth.user', related_name='%(app_label)s_%(class)s_creator', verbose_name='creator')

    @staticmethod
    def verbose():
        return u'运维追踪事务'
    class Meta:
        ordering=['-created_date']


class Item_list(CommonModel,ITEM_BASE):
    item=models.ForeignKey(Item_name)
    app=models.ForeignKey(Site,blank=True,null=True,related_name='site')
    upstream=models.CharField(max_length=200,blank=True)
    tech=models.ForeignKey(Tech,related_name='tech')
    front=models.ManyToManyField(Ipv4Address,blank=True,related_name='front')
    app_link=models.ManyToManyField(Application,blank=True,related_name='app')
    mysql_link=models.ManyToManyField(Mysql,blank=True,related_name='mysql')
    redis_link=models.ManyToManyField(Redis,blank=True,related_name='redis')
    codis_link=models.ManyToManyField(Codis,blank=True,related_name='codis')
    sentinel=models.ManyToManyField(Sentinel,blank=True,related_name='sentinel')
    zookeeper=models.ManyToManyField(Zookeeper,blank=True,related_name='zookeeper')
    kafka=models.ManyToManyField(Kafka,blank=True,related_name='kafka')
    mq=models.ManyToManyField(RocketMQ,blank=True,related_name='mq')
    memcache=models.ManyToManyField(Memcached,blank=True,related_name='memcache')
    es=models.ManyToManyField(Es,blank=True,related_name='es')
    mcq=models.ManyToManyField(Mcq,blank=True,related_name='mcq')
    tfs=models.ManyToManyField(Tfs,blank=True,related_name='tfs')
    app_location=models.CharField(max_length=200,blank=True,null=True)
    remark=models.TextField(blank=True)

    @staticmethod
    def verbose():
        return u'项目部署详情'

class Check_type(CommonModel,API_BASE):
    content=models.CharField(max_length=50,unique=True)
    alias=models.CharField(max_length=50,unique=True)
    def __unicode__(self):
        return self.content

    @staticmethod
    def verbose():
        return u'测试类型'

class Item_check(CommonModel,ITEM_BASE):
    Check_status = (
         (0, u'正常'),
         (1, u'异常'),
    )
    item=models.ForeignKey(Item_name)
    type=models.ForeignKey(Check_type)
    status=models.IntegerField(choices=Check_status)
    method=models.CharField(max_length=50,blank=True)
    headers=models.CharField(max_length=250,blank=True)
    port=models.IntegerField()
    content=models.CharField(max_length=250,blank=True)
    link_address=models.CharField(max_length=250)
    retcode=models.CharField(max_length=50,blank=True)
    result=models.CharField(max_length=250,blank=True)
    remark=models.TextField(blank=True)

    @staticmethod
    def verbose():
        return u'测试类型'


# class Kvm_list(CommonModel,APPLY_BASE):
#     idc=models.CharField(max_length=200)
#     zone=models.CharField(max_length=200)
#     item=models.ForeignKey(Item_name)
#     @staticmethod
#     def verbose():
#         return u'KVM'
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
