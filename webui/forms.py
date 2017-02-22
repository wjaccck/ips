# #coding=utf8
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.utils.translation import ugettext_lazy as _
from api.models import *
from .wiget import *

class LoginForm(AuthenticationForm):
    '''Authentication form which uses boostrap CSS.'''
    username = forms.CharField(max_length=255,widget=forms.TextInput({
                                   'class': 'form-control'}))
    password = forms.CharField(label=_('Password'),
                               widget=forms.PasswordInput({
                                   'class': 'form-control'}))



class MachineForm(forms.ModelForm):
    name=forms.CharField(label='name',max_length=100,widget=forms.TextInput({'class': 'form-control'}))
    memory=forms.IntegerField(label='memory',required=False,widget=forms.TextInput({'class': 'form-control'}))
    cpu=forms.IntegerField(label='cpu',required=False,widget=forms.TextInput({'class': 'form-control'}))
    disk_info=forms.CharField(label='disk_info',required=False,widget=forms.TextInput({'class': 'form-control'}))
    product=forms.CharField(label='product',max_length=100,widget=forms.TextInput({'class': 'form-control'}))
    system_id=forms.CharField(label='system',max_length=50,widget=forms.TextInput({'class': 'form-control'}))
    machine_id=forms.CharField(label='machine_id',max_length=200,required=False,widget=forms.TextInput({'class': 'form-control'}))
    serial=forms.CharField(label='serial',required=False,max_length=200,widget=forms.TextInput({'class': 'form-control'}))
    major_release=forms.CharField(label='主版本',max_length=50,widget=forms.TextInput({'class': 'form-control'}))
    sys_desc=forms.CharField(label='详细版本',max_length=50,widget=forms.TextInput({'class': 'form-control'}))
    idc=forms.CharField(label='数据中心',max_length=50,widget=forms.TextInput({'class': 'form-control'}))
    company=forms.CharField(label='所属公司',max_length=50,widget=forms.TextInput({'class': 'form-control'}))

    class Meta:
        model = Machine
        fields = (
            'mark',
            'ips',
            'name',
            'memory',
            'cpu',
            'disk_info',
            'product',
            'system_id',
            'machine_id',
            'serial',
            'major_release',
            'sys_desc',
            'idc',
            'company',
        )
        widgets = {
            'ips': IpsModelSelect2MultipleWidget,
            'mark': IpModelSelect2Widget,
        }

class SiteForm(forms.ModelForm):

    content = forms.CharField(label='content', max_length=255, widget=forms.TextInput({'class': 'form-control'}))
    alias = forms.CharField(label='alias', max_length=255,  widget=forms.TextInput({'class': 'form-control'}))

    class Meta:
        model = Site
        exclude = ['created_date', 'modified_date']



class Nginx_infoForm(forms.ModelForm):
    file_name=forms.CharField(label='name',max_length=200,widget=forms.TextInput({'class': 'form-control'}))
    class Meta:
        model = Nginx
        fields = (
            'host',
            'type',
            'app_name',
            'file_name',
        )
        widgets = {
            'host':IpModelSelect2Widget,
            'type':TypeModelSelect2Widget,
            'app_name': App_namesModelSelect2MultipleWidget,
        }


class TechForm(forms.ModelForm):

    content = forms.CharField(label='content', max_length=255, widget=forms.TextInput({'class': 'form-control'}))
    alias = forms.CharField(label='alias', max_length=255,  widget=forms.TextInput({'class': 'form-control'}))

    class Meta:
        model = Tech
        fields = (
            'content',
            'alias',
        )
        exclude = ['created_date', 'modified_date']


class MysqlForm(forms.ModelForm):
    name = forms.CharField(label='name', max_length=50, widget=forms.TextInput({'class': 'form-control'}))
    port = forms.CharField(label='port',  max_length=50,widget=forms.TextInput({'class': 'form-control'}))
    detail = forms.CharField(label='detail',required=False, max_length=255,widget=forms.TextInput({'class': 'form-control'}))

    class Meta:
        model = Mysql
        fields = (
            'name',
            'host',
            'port',
            'detail',
            'slaveof'
        )
        widgets = {
            'host':IpModelSelect2Widget,
            'slaveof':IpsModelSelect2MultipleWidget,
        }
        exclude = ['created_date', 'modified_date']


class ApplicationForm(forms.ModelForm):
    port = forms.CharField(label='port',   max_length=50,widget=forms.TextInput({'class': 'form-control'}))
    detail = forms.CharField(label='detail',required=False, max_length=255,widget=forms.TextInput({'class': 'form-control'}))

    class Meta:
        model = Application
        fields = (
            'host',
            'port',
            'detail',
        )
        widgets = {
            'host':IpModelSelect2Widget,
        }
        exclude = ['created_date', 'modified_date']

class CodisForm(forms.ModelForm):
    port = forms.CharField(label='port',   max_length=50,widget=forms.TextInput({'class': 'form-control'}))
    detail = forms.CharField(label='detail',required=False, max_length=255,widget=forms.TextInput({'class': 'form-control'}))

    class Meta:
        model = Codis
        fields = (
            'host',
            'port',
            'detail',
            'slaveof',
        )
        widgets = {
            'host':IpModelSelect2Widget,
             'slaveof':IpsModelSelect2MultipleWidget,
        }
        exclude = ['created_date', 'modified_date']


class RedisForm(forms.ModelForm):
    port = forms.CharField(label='port',   max_length=50,widget=forms.TextInput({'class': 'form-control'}))
    detail = forms.CharField(label='detail',required=False, max_length=255,widget=forms.TextInput({'class': 'form-control'}))

    class Meta:
        model = Redis
        fields = (
            'host',
            'port',
            'detail',
            'slaveof',
        )
        widgets = {
            'host':IpModelSelect2Widget,
             'slaveof':IpsModelSelect2MultipleWidget,
        }
        exclude = ['created_date', 'modified_date']

class SentinelForm(forms.ModelForm):
    port = forms.CharField(label='port',   max_length=50,widget=forms.TextInput({'class': 'form-control'}))
    detail = forms.CharField(label='detail',required=False, max_length=255,widget=forms.TextInput({'class': 'form-control'}))

    class Meta:
        model = Sentinel
        fields = (
            'host',
            'port',
            'detail',
            'slaveof',
        )
        widgets = {
            'host':IpModelSelect2Widget,
             'slaveof':IpsModelSelect2MultipleWidget,
        }
        exclude = ['created_date', 'modified_date']

class MemcachedForm(forms.ModelForm):
    port = forms.CharField(label='port',   max_length=50,widget=forms.TextInput({'class': 'form-control'}))
    detail = forms.CharField(label='detail',required=False, max_length=255,widget=forms.TextInput({'class': 'form-control'}))

    class Meta:
        model = Memcached
        fields = (
            'host',
            'port',
            'detail',
        )
        widgets = {
            'host':IpModelSelect2Widget,
        }
        exclude = ['created_date', 'modified_date']

class EsForm(forms.ModelForm):
    port = forms.CharField(label='port',   max_length=50,widget=forms.TextInput({'class': 'form-control'}))
    detail = forms.CharField(label='detail',required=False, max_length=255,widget=forms.TextInput({'class': 'form-control'}))

    class Meta:
        model = Es
        fields = (
            'host',
            'port',
            'detail',
        )
        widgets = {
            'host':IpModelSelect2Widget,
        }
        exclude = ['created_date', 'modified_date']

class McqForm(forms.ModelForm):
    port = forms.CharField(label='port',   max_length=50,widget=forms.TextInput({'class': 'form-control'}))
    detail = forms.CharField(label='detail',required=False, max_length=255,widget=forms.TextInput({'class': 'form-control'}))

    class Meta:
        model = Mcq
        fields = (
            'host',
            'port',
            'detail',
        )
        widgets = {
            'host':IpModelSelect2Widget,
        }
        exclude = ['created_date', 'modified_date']

class ZookeeperForm(forms.ModelForm):
    port = forms.CharField(label='port',   max_length=50,widget=forms.TextInput({'class': 'form-control'}))

    class Meta:
        model = Zookeeper
        fields = (
            'host',
            'port',
        )
        widgets = {
            'host':IpModelSelect2Widget,
        }
        exclude = ['created_date', 'modified_date']

class KafkaForm(forms.ModelForm):
    port = forms.CharField(label='port',   max_length=50,widget=forms.TextInput({'class': 'form-control'}))

    class Meta:
        model = Kafka
        fields = (
            'host',
            'port',
        )
        widgets = {
            'host':IpModelSelect2Widget,
        }
        exclude = ['created_date', 'modified_date']

class MqForm(forms.ModelForm):
    port = forms.CharField(label='port',   max_length=50,widget=forms.TextInput({'class': 'form-control'}))

    class Meta:
        model = RocketMQ
        fields = (
            'host',
            'port',
        )
        widgets = {
            'host':IpModelSelect2Widget,
        }
        exclude = ['created_date', 'modified_date']



class TfsForm(forms.ModelForm):
    port = forms.CharField(label='port',   max_length=50,widget=forms.TextInput({'class': 'form-control'}))
    detail = forms.CharField(label='detail',required=False, max_length=255,widget=forms.TextInput({'class': 'form-control'}))

    class Meta:
        model = Tfs
        fields = (
            'host',
            'port',
            'detail',
        )
        widgets = {
            'host':IpModelSelect2Widget,
        }
        exclude = ['created_date', 'modified_date']


class Item_nameForm(forms.ModelForm):
    content = forms.CharField(label='content', max_length=50, widget=forms.TextInput({'class': 'form-control'}))
    module = forms.CharField(label='module', required=False,max_length=50, widget=forms.TextInput({'class': 'form-control'}))
    alias = forms.CharField(label='alias',max_length=50, required=False,widget=forms.TextInput({'class': 'form-control'}))
    dev_owner = forms.CharField(label='dev_owner', required=False,max_length=200, widget=forms.TextInput({'class': 'form-control'}))
    ops_owner = forms.CharField(label='ops_owner', required=False,max_length=200, widget=forms.TextInput({'class': 'form-control'}))
    test_owner = forms.CharField(label='test_owner', required=False,max_length=200, widget=forms.TextInput({'class': 'form-control'}))
    git_url = forms.CharField(label='git_url', required=False,max_length=200, widget=forms.TextInput({'class': 'form-control'}))
    location = forms.CharField(label='location', required=False,max_length=250, widget=forms.TextInput({'class': 'form-control'}))

    class Meta:
        model = Item_name
        exclude = ['created_date', 'modified_date']

class Item_listForm(forms.ModelForm):

    class Meta:
        model = Item_list
        fields = (
            'item',
            'app',
            'upstream',
            'tech',
            'front',
            'app_link',
            'mysql_link',
            'redis_link',
            'codis_link',
            'sentinel',
            'memcache',
            'es',
            'mcq',
            'tfs',
            'zookeeper',
            'kafka',
            'mq',
            'remark',
        )
        widgets = {
            'item':Item_nameModelSelect2Widget,
            'app':App_nameModelSelect2Widget,
            'tech':Tech_typeModelSelect2Widget,
            'front':IpsModelSelect2MultipleWidget,
            'app_link':App_linksModelSelect2MultipleWidget,
            'mysql_link':Mysql_linksModelSelect2MultipleWidget,
            'redis_link':Redis_linksModelSelect2MultipleWidget,
            'codis_link':Codis_linksModelSelect2MultipleWidget,
            'sentinel':SentinelModelSelect2MultipleWidget,
            'memcache':MemcacheModelSelect2MultipleWidget,
            'es':EsModelSelect2MultipleWidget,
            'mcq':McqModelSelect2MultipleWidget,
            'tfs':TfsModelSelect2MultipleWidget,
            'zookeeper':ZookeeperModelSelect2MultipleWidget,
            'kafka':KafkaModelSelect2MultipleWidget,
            'mq':MQModelSelect2MultipleWidget,
        }
        exclude = ['created_date', 'modified_date']


class Item_checkForm(forms.ModelForm):
    method = forms.CharField(label='method',   required=False,max_length=50,widget=forms.TextInput({'class': 'form-control'}))
    headers = forms.CharField(label='headers',   required=False,max_length=50,widget=forms.TextInput({'class': 'form-control'}))
    link_address = forms.CharField(label='link_address',   max_length=50,widget=forms.TextInput({'class': 'form-control'}))
    content = forms.CharField(label='content',   required=False,max_length=50,widget=forms.TextInput({'class': 'form-control'}))
    port = forms.CharField(label='port',   max_length=50,widget=forms.TextInput({'class': 'form-control'}))
    retcode = forms.CharField(label='retcode',   required=False,max_length=50,widget=forms.TextInput({'class': 'form-control'}))
    result = forms.CharField(label='result',   required=False,max_length=50,widget=forms.TextInput({'class': 'form-control'}))

    class Meta:
        model = Item_check
        fields = (
            'item',
            'type',
            'status',
            'method',
            'headers',
            'link_address',
            'content',
            'port',
            'retcode',
            'result',
            'remark'
        )
        widgets = {
            'item':Item_nameModelSelect2Widget,
            'type':App_nameModelSelect2Widget,
        }
        exclude = ['created_date', 'modified_date']


class Docker_listForm(forms.ModelForm):
    app = forms.CharField(label='app', max_length=200, widget=forms.TextInput({'class': 'form-control'}))
    remark = forms.CharField(label='remark', required=False,max_length=200, widget=forms.TextInput({'class': 'form-control'}))
    class Meta:
        model = Docker_list
        fields = (
            'host',
            'tech',
            'item',
            'app',
            'remark',
        )
        widgets = {
            'host':IpModelSelect2Widget,
            'item':Item_nameModelSelect2Widget,
            'tech':Tech_typeModelSelect2Widget,
        }
        exclude = ['created_date', 'modified_date']



class Ops_act_historyForm(forms.ModelForm):
    title = forms.ChoiceField(label='类型',choices=[
        ('配置更改','配置更改'),
        ('版本发布','版本发布'),
        ('数据修改','数据修改'),
        ('其他','其他')
    ])
    # title = forms.CharField(label='主题', max_length=50, widget=forms.TextInput({'class': 'form-control'}))
    operator = forms.CharField(label='操作者', max_length=50, widget=forms.TextInput({'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        self.creator = kwargs.pop('creator', None)
        super(Ops_act_historyForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(Ops_act_historyForm, self).save(commit=False)
        if self.creator:
            instance.creator = self.creator
        return instance.save()

    class Meta:
        fields = (
            'title',
            'operator',
            'content',
        )
        model = Ops_act_history
        exclude = ['created_date', 'modified_date']


class Ops_plan_historyForm(forms.ModelForm):
    # title = forms.CharField(label='主题', max_length=50, widget=forms.TextInput({'class': 'form-control'}))
    operator = forms.CharField(label='负责人', max_length=50, widget=forms.TextInput({'class': 'form-control'}))
    status = forms.ChoiceField(label='状态',choices=[
        ('进行中','进行中'),
        ('结束','结束')
    ])
    def __init__(self, *args, **kwargs):
        self.creator = kwargs.pop('creator', None)
        super(Ops_plan_historyForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(Ops_plan_historyForm, self).save(commit=False)
        if self.creator:
            instance.creator = self.creator
        return instance.save()

    class Meta:
        fields = (
            'title',
            'operator',
            'content',
            'status',
        )
        model = Ops_plan_history
        exclude = ['created_date', 'modified_date']