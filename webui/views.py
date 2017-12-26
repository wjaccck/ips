#coding=utf8
from django.shortcuts import render,redirect
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
# from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from core.common import logger
from django.db.models import Q
from api.models import *
from vanilla import ListView, CreateView, UpdateView, DeleteView,FormView
from django.http import HttpResponse,HttpResponseBadRequest,HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
import forms
from django.views.generic import TemplateView,View
# import datetime
import json
from core.common import logger,get_result
import operator
from rest_framework.decorators import api_view, permission_classes
from api.tasks import MissionTask
from rest_framework.views import APIView


class Process_ViewSet(APIView):
    http_method_names = ['post']
    permission_classes = (permissions.IsAuthenticated,)
    model = Machine_procs
    def post(self, request):
        try:
            content = request.POST.get('data')
            data=json.loads(content)
            host=data.get('host')
            machine=Machine.objects.get(console_ip__name=host)
            Machine_procs.objects.filter(host=machine).delete()
            querysetlist = []
            for i in data.get('procs'):
                querysetlist.append(Machine_procs(host=machine,
                                                  pid=i.get('pid'),
                                                  name=i.get('name'),
                                                  username=i.get('username')
                                                  )
                                    )
            try:
                Machine_procs.objects.bulk_create(querysetlist)
                return HttpResponse(json.dumps(get_result(0,'add')))
            except Exception as e:
                return HttpResponseBadRequest(json.dumps(get_result(1, str(e))))
        except:
            return HttpResponseBadRequest(json.dumps(get_result(1,'no data in the body')))
    # def get(self,request):
    #     try:
    #         host = request.GET.get('host')
    #     except:
    #         host=None
    #
    #     if host:
    #         return HttpResponse(json.dumps([{'content':x.content} for x in self.model.objects.filter(content__istartswith=content)]))
    #     else:
    #         return HttpResponse(json.dumps([{'alias':x.alias} for x in self.model.objects.all()]))

    def post(self, request):
        try:
            content = request.POST.get('content')
        except:
            content = None

        print(content)
        if content:
            return HttpResponse(json.dumps(
                [{'content': x.content} for x in self.model.objects.filter(content__istartswith=content)]))
        else:
            return HttpResponse(json.dumps([{'alias': x.alias} for x in self.model.objects.all()]))


def format_response(result):
    logger.info('result: %s' % result)
    if result:
        return HttpResponse(json.dumps(result))
    else:
        return HttpResponse(json.dumps(get_result(1, 'error request')))

class BaseViewAdmin(APIView):
    http_method_names = ['post']
    permission_classes = (permissions.IsAuthenticated,)

    def init(self, request):
        pass

    def run(self):
        pass

    def post(self, request, *args, **kwargs):
        self.init(request)
        return format_response(self.run())

    def get(self, request, *args, **kwargs):
        return self.post(request)


class MissionBaseViewAdmin(BaseViewAdmin):
    project=None
    module=None
    environment=None
    version=None
    build=None
    file_name=None
    file_url=None
    file_md5=None
    config_name=None
    config_url=None
    config_md5=None

    def init(self, request):
        super(MissionBaseViewAdmin, self).init(request)
        self.project = request.POST.get('project')
        self.module = request.POST.get('module')
        self.environment = request.POST.get('environment')
        self.version = request.POST.get('version')
        self.build = request.POST.get('build')
        self.file_name = request.POST.get('file_name')
        self.file_url = request.POST.get('file_url')
        self.file_md5 = request.POST.get('file_md5')
        self.config_name = request.POST.get('config_name')
        self.config_url = request.POST.get('config_url')
        self.config_md5 = request.POST.get('config_md5')

class Get_VersionViewAdmin(BaseViewAdmin):
    def run(self):
        module=None
        try:
            module=self.request.GET['module']
        except:
            pass
        if module:
            try:
                todo_version=Version_history.objects.get(module=module,latest_status=True)
                send_data={
                    "version":todo_version.version,
                    "file_url":todo_version.file_url,
                    "file_md5":todo_version.file_md5,
                    "config_url":todo_version.config_url,
                    "config_md5":todo_version.config_md5
                }
                return HttpResponse(json.dumps(get_result(0,send_data)))
            except Exception,e:
                return HttpResponseBadRequest(json.dumps(get_result(1,str(e))))
        else:
            return HttpResponseBadRequest(json.dumps(get_result(2,'no module send to filter')))

class Create_VersionViewAdmin(MissionBaseViewAdmin):
    def run(self):
        try:
            module=Item_name.objects.get(module=self.module)
            Version_history.objects.filter(module=module,version=self.version).update(latest_status=False)
            Version_history.objects.create(
                project=self.project,
                module=module,
                environment=self.environment,
                version=self.version,
                build=self.build,
                file_name=self.file_name,
                file_url=self.file_url,
                file_md5=self.file_md5,
                config_name=self.config_name,
                config_url=self.config_url,
                config_md5=self.config_md5,
                latest_status=True
            )
            return get_result(0,'done')
        except Exception,e:
            return get_result(1,str(e))

def index(req):
    if req.user.is_authenticated():
        idc_list=['hz','qs']
        all_count=Machine.objects.filter(company='shihui').count()
        product_list=[ x.get('product') for x in Machine.objects.filter(company='shihui').values('product').distinct()]
        product=[{"name":x,"number":Machine.objects.filter(company='shihui',product=x).count()} for x in product_list]
        sys_list=[ x.get('distribution_version') for x in Machine.objects.filter(company='shihui').values('distribution_version').distinct()]
        sys=[{"name":x,"number":Machine.objects.filter(company='shihui',distribution_version=x).count()} for x in sys_list]
        idc_detail=[{"name":x,"number":Machine.objects.filter(company='shihui',idc=x).count()} for x in idc_list]
        dev_owner=[ x.get('dev_owner') for x in Item_name.objects.all().values('dev_owner').distinct()]
        item_summary=[{"name":x,"number":Item_name.objects.filter(dev_owner=x).count()} for x in dev_owner]

        response = render(req,'webui/index.html',{"username":req.user.last_name,
                                                  "active":"index",
                                                  "total_list":all_count,
                                                  "product":product,
                                                  "sys":sys,
                                                  "idc_detail":idc_detail,
                                                  "item_summary":item_summary,
                                                  }
                          )
    else:
        response =redirect('login')
    return response

class Base_ListViewSet(ListView):

    def get_context_data(self, **kwargs):
        context = super(Base_ListViewSet, self).get_context_data(**kwargs)
        context['create'] = u'创建'
        context['btnsubmit'] = u'提交'
        context['btncancel'] = u'取消'
        context['item']=self.model.verbose()
        context['username']=self.request.user.last_name
        context['is_superuser']=self.request.user.is_superuser
        context['active']=self.model.father()
        # context['hello'] = u'欢迎回来, '
        # context['login'] = u'登录'
        # context['logout'] = u'注销'
        # if self.request.user.is_superuser:
        #     item_list=[x.__name__ for x in get_models(get_app('api'))]
        # else:
        #     item_list=['List']
        # context['item_list']=item_list
        # context['api']=item_list
        # if self.model.__name__ in item_list:

        # else:
        #     context['active']='index'
        return context

class Base_CreateViewSet(CreateView):

    def get_context_data(self, **kwargs):
        context = super(Base_CreateViewSet, self).get_context_data(**kwargs)
        context['create'] = u'创建'
        context['btnsubmit'] = u'提交'
        context['btncancel'] = u'取消'
        context['item']=self.model.verbose()
        context['username']=self.request.user.last_name
        context['is_superuser']=self.request.user.is_superuser
        context['active']=self.model.father()
        return context

class Base_UpdateViewSet(UpdateView):

    def get_context_data(self, **kwargs):
        context = super(Base_UpdateViewSet, self).get_context_data(**kwargs)
        context['create'] = u'创建'
        context['btnsubmit'] = u'提交'
        context['btncancel'] = u'取消'
        context['item']=self.model.verbose()
        context['username']=self.request.user.last_name
        context['is_superuser']=self.request.user.is_superuser
        context['active']=self.model.father()
        return context

class Machine_proc_ViewSet(Base_ListViewSet):
    Machine_procs.objects.all().count()
    model = Machine_procs
    template_name = 'api/proc.html'
    paginate_by = 10

    def get_queryset(self):
        # support search
        try:
            keyword = self.request.GET['keyword']
        except:
            keyword = None
        try:
            host = self.request.GET['host']
        except:
            host = None

        if keyword :
            if host:
                return self.model.objects.filter(host=Machine.objects.get(console_ip__name=host),name__icontains=keyword)
            else:
                return self.model.objects.filter(name__icontains=keyword)
        else:
            if host:
                return self.model.objects.filter(host=Machine.objects.get(console_ip__name=host))
            else:
                return self.model.objects.all()


class Machine_createViewSet(Base_CreateViewSet):
    model = Machine
    form_class = forms.MachineForm
    template_name = 'api/machine_form.html'
    success_url = reverse_lazy('machine-list')

class Machine_updateViewSet(Base_UpdateViewSet):
    model = Machine
    form_class = forms.MachineForm
    template_name = 'api/machine_form.html'
    success_url = reverse_lazy('machine-list')

class Machine_listViewSet(Base_ListViewSet):
    Machine.objects.all().count()
    model = Machine
    template_name = 'api/machine.html'
    paginate_by = 10

    def get_queryset(self):
        try:
            idc=self.request.GET['idc']
        except:
            idc=''
        query_list=[]
        if idc:
            query_list.append(Q(idc=idc))
        try:
            ip=self.request.GET['ip']
            query_list.append(Q(ipv4__name__istartswith=ip))
        except:
            pass
        try:
            sys_desc=self.request.GET['sys']
            query_list.append(Q(distribution_version__istartswith=sys_desc))
        except:
            pass
        try:
            company=self.request.GET['company']
            query_list.append(Q(company=company))
        except:
            pass
        if query_list:
            return list(set(Machine.objects.select_related().filter(reduce(operator.and_, query_list))))
        else:
            return Machine.objects.select_related().all()

class Site_ViewSet(Base_ListViewSet):
    Site.objects.all().count()
    model = Site
    template_name = 'api/site.html'
    paginate_by = 10

    def get_queryset(self):
        # support search
        try:
            keyword = self.request.GET['keyword']
        except:
            keyword = ''
        if keyword == '':
            return Site.objects.all()
        else:
            return Site.objects.filter(content__icontains=keyword)

class Site_CreateViewSet(Base_CreateViewSet):
    model = Site
    form_class = forms.SiteForm
    template_name = 'api/site_form.html'

    success_url = reverse_lazy('site-list')

class Site_UpdateViewSet(Base_UpdateViewSet):
    model = Site
    form_class = forms.SiteForm
    success_url = reverse_lazy('site-list')
    template_name = 'api/site_form.html'

class Nginx_ViewSet(Base_ListViewSet):
    Nginx.objects.all().count()
    model = Nginx
    template_name = 'api/nginx.html'
    paginate_by = 10

    def get_queryset(self):
        query_list=[]
        try:
            ip=self.request.GET['ip']
            query_list.append(Q(host=Ipv4Address.objects.get(name=ip)))
        except:
            pass
        try:
            app=self.request.GET['app']
            query_list.append(Q(app_name__content__icontains=app))
        except:
            pass

        if query_list:
            return Nginx.objects.select_related().filter(reduce(operator.and_, query_list))
        else:
            return Nginx.objects.select_related().all()

class Nginx_CreateViewSet(Base_CreateViewSet):
    model = Nginx
    form_class = forms.Nginx_infoForm
    template_name = 'api/nginx_form.html'

    success_url = reverse_lazy('nginx-list')

class Nginx_UpdateViewSet(Base_UpdateViewSet):
    model = Nginx
    form_class = forms.Nginx_infoForm
    success_url = reverse_lazy('nginx-list')
    template_name = 'api/nginx_form.html'

class Tech_ViewSet(Base_ListViewSet):
    Tech.objects.all().count()
    model = Tech
    template_name = 'api/tech.html'
    paginate_by = 10

    def get_queryset(self):
        try:
            keyword=self.request.GET['keyword']
        except:
            keyword=''

        if keyword:
            return Tech.objects.filter(content__icontains=keyword)
        else:
            return Tech.objects.all()

class Tech_CreateViewSet(Base_CreateViewSet):
    model = Tech
    form_class = forms.TechForm
    template_name = 'api/tech_form.html'
    success_url = reverse_lazy('tech-list')

class Tech_UpdateViewSet(Base_UpdateViewSet):
    model = Tech
    form_class = forms.TechForm
    success_url = reverse_lazy('tech-list')
    template_name = 'api/tech_form.html'


class Mysql_ViewSet(Base_ListViewSet):
    Mysql.objects.all().count()
    model = Mysql
    template_name = 'api/mysql.html'
    paginate_by = 10

    def get_queryset(self):
        try:
            keyword=self.request.GET['keyword']
        except:
            keyword=''
        query_list=[]
        if keyword:
            query_list.append(Q(host__name=keyword)|Q(slaveof__name=keyword))
        try:
            name=self.request.GET['name']
            query_list.append(Q(name__icontains=name))
        except:
            pass
        try:
            port=self.request.GET['port']
            query_list.append(Q(port__exact=port))
        except:
            pass
        if query_list:
            return list(set(Mysql.objects.select_related().filter(reduce(operator.and_, query_list))))
        else:
            return Mysql.objects.all()

class Mysql_CreateViewSet(Base_CreateViewSet):
    model = Mysql
    form_class = forms.MysqlForm
    template_name = 'api/mysql_form.html'
    success_url = reverse_lazy('mysql-list')

class Mysql_UpdateViewSet(Base_UpdateViewSet):
    model = Mysql
    form_class = forms.MysqlForm
    template_name = 'api/mysql_form.html'
    success_url = reverse_lazy('mysql-list')

class Application_ViewSet(Base_ListViewSet):
    Application.objects.all().count()
    model = Application
    template_name = 'api/application.html'
    paginate_by = 10

    def get_queryset(self):
        try:
            keyword=self.request.GET['keyword']
        except:
            keyword=''

        if keyword:
            return Application.objects.select_related().filter(host__name=keyword)
        else:
            return Application.objects.all()

class Application_CreateViewSet(Base_CreateViewSet):
    model = Application
    form_class = forms.ApplicationForm
    template_name = 'api/application_form.html'
    success_url = reverse_lazy('application-list')

class Application_UpdateViewSet(Base_UpdateViewSet):
    model = Application
    form_class = forms.ApplicationForm
    success_url = reverse_lazy('application-list')
    template_name = 'api/application_form.html'

class Codis_ViewSet(Base_ListViewSet):
    Codis.objects.all().count()
    model = Codis
    template_name = 'api/codis.html'
    paginate_by = 10

    def get_queryset(self):
        try:
            keyword=self.request.GET['keyword']
        except:
            keyword=''

        if keyword:
            return Codis.objects.select_related().filter(Q(host__name=keyword)|Q(slaveof__name=keyword))
        else:
            return Codis.objects.all()

class Codis_CreateViewSet(Base_CreateViewSet):
    model = Codis
    form_class = forms.CodisForm
    template_name = 'api/codis_form.html'
    success_url = reverse_lazy('codis-list')

class Codis_UpdateViewSet(Base_UpdateViewSet):
    model = Codis
    form_class = forms.CodisForm
    success_url = reverse_lazy('codis-list')
    template_name = 'api/codis_form.html'

class Redis_ViewSet(Base_ListViewSet):
    Redis.objects.all().count()
    model = Redis
    template_name = 'api/redis.html'
    paginate_by = 10

    def get_queryset(self):
        try:
            keyword=self.request.GET['keyword']
        except:
            keyword=''

        if keyword:
            return Redis.objects.select_related().filter(Q(host__name=keyword)|Q(slaveof__name=keyword))
        else:
            return Redis.objects.all()

class Redis_CreateViewSet(Base_CreateViewSet):
    model = Redis
    form_class = forms.RedisForm
    template_name = 'api/redis_form.html'
    success_url = reverse_lazy('redis-list')

class Redis_UpdateViewSet(Base_UpdateViewSet):
    model = Redis
    form_class = forms.RedisForm
    success_url = reverse_lazy('redis-list')
    template_name = 'api/redis_form.html'

class Sentinel_ViewSet(Base_ListViewSet):
    Sentinel.objects.all().count()
    model = Sentinel
    template_name = 'api/sentinel.html'
    paginate_by = 10

    def get_queryset(self):
        try:
            keyword=self.request.GET['keyword']
        except:
            keyword=''

        if keyword:
            return Sentinel.objects.select_related().filter(Q(host__name=keyword)|Q(slaveof__name=keyword))
        else:
            return Sentinel.objects.all()

class Sentinel_CreateViewSet(Base_CreateViewSet):
    model = Sentinel
    form_class = forms.SentinelForm
    template_name = 'api/sentinel_form.html'
    success_url = reverse_lazy('sentinel-list')

class Sentinel_UpdateViewSet(Base_UpdateViewSet):
    model = Sentinel
    form_class = forms.SentinelForm
    success_url = reverse_lazy('sentinel-list')
    template_name = 'api/sentinel_form.html'

class Memcache_ViewSet(Base_ListViewSet):
    Memcached.objects.all().count()
    model = Memcached
    template_name = 'api/memcache.html'
    paginate_by = 10

    def get_queryset(self):
        try:
            keyword=self.request.GET['keyword']
        except:
            keyword=''

        if keyword:
            return Memcached.objects.select_related().filter(host__name=keyword)
        else:
            return Memcached.objects.all()

class Memcache_CreateViewSet(Base_CreateViewSet):
    model = Memcached
    form_class = forms.MemcachedForm
    template_name = 'api/memcache_form.html'
    success_url = reverse_lazy('memcache-list')

class Memcache_UpdateViewSet(Base_UpdateViewSet):
    model = Memcached
    form_class = forms.MemcachedForm
    success_url = reverse_lazy('memcache-list')
    template_name = 'api/memcache_form.html'

class Es_ViewSet(Base_ListViewSet):
    Es.objects.all().count()
    model = Es
    template_name = 'api/es.html'
    paginate_by = 10

    def get_queryset(self):
        try:
            keyword=self.request.GET['keyword']
        except:
            keyword=''

        if keyword:
            return Es.objects.select_related().filter(host__name=keyword)
        else:
            return Es.objects.all()

class Es_CreateViewSet(Base_CreateViewSet):
    model = Es
    form_class = forms.EsForm
    template_name = 'api/es_form.html'
    success_url = reverse_lazy('es-list')

class Es_UpdateViewSet(Base_UpdateViewSet):
    model = Es
    form_class = forms.EsForm
    success_url = reverse_lazy('es-list')
    template_name = 'api/es_form.html'

class Mcq_ViewSet(Base_ListViewSet):
    Mcq.objects.all().count()
    model = Mcq
    template_name = 'api/mcq.html'
    paginate_by = 10

    def get_queryset(self):
        try:
            keyword=self.request.GET['keyword']
        except:
            keyword=''

        if keyword:
            return Mcq.objects.select_related().filter(host__name=keyword)
        else:
            return Mcq.objects.all()

class Mcq_CreateViewSet(Base_CreateViewSet):
    model = Mcq
    form_class = forms.McqForm
    template_name = 'api/mcq_form.html'
    success_url = reverse_lazy('mcq-list')

class Mcq_UpdateViewSet(Base_UpdateViewSet):
    model = Mcq
    form_class = forms.McqForm
    success_url = reverse_lazy('mcq-list')
    template_name = 'api/mcq_form.html'

class Tfs_ViewSet(Base_ListViewSet):
    Tfs.objects.all().count()
    model = Tfs
    template_name = 'api/tfs.html'
    paginate_by = 10

    def get_queryset(self):
        try:
            keyword=self.request.GET['keyword']
        except:
            keyword=''

        if keyword:
            return Tfs.objects.select_related().filter(host__name=keyword)
        else:
            return Tfs.objects.all()

class Tfs_CreateViewSet(Base_CreateViewSet):
    model = Tfs
    form_class = forms.TfsForm
    template_name = 'api/tfs_form.html'
    success_url = reverse_lazy('tfs-list')

class Tfs_UpdateViewSet(Base_UpdateViewSet):
    model = Tfs
    form_class = forms.TfsForm
    success_url = reverse_lazy('tfs-list')
    template_name = 'api/tfs_form.html'

class Zookeeper_ViewSet(Base_ListViewSet):
    Zookeeper.objects.all().count()
    model = Zookeeper
    template_name = 'api/zookeeper.html'
    paginate_by = 10

    def get_queryset(self):
        try:
            keyword=self.request.GET['keyword']
        except:
            keyword=''

        if keyword:
            return Zookeeper.objects.select_related().filter(host__name=keyword)
        else:
            return Zookeeper.objects.all()

class Zookeeper_CreateViewSet(Base_CreateViewSet):
    model = Zookeeper
    form_class = forms.ZookeeperForm
    template_name = 'api/zookeeper_form.html'
    success_url = reverse_lazy('zookeeper-list')

class Zookeeper_UpdateViewSet(Base_UpdateViewSet):
    model = Zookeeper
    form_class = forms.ZookeeperForm
    success_url = reverse_lazy('zookeeper-list')
    template_name = 'api/zookeeper_form.html'


class Kafka_ViewSet(Base_ListViewSet):
    Kafka.objects.all().count()
    model = Kafka
    template_name = 'api/kafka.html'
    paginate_by = 10

    def get_queryset(self):
        try:
            keyword=self.request.GET['keyword']
        except:
            keyword=''

        if keyword:
            return Kafka.objects.select_related().filter(host__name=keyword)
        else:
            return Kafka.objects.all()

class Kafka_CreateViewSet(Base_CreateViewSet):
    model = Kafka
    form_class = forms.KafkaForm
    template_name = 'api/kafka_form.html'
    success_url = reverse_lazy('kafka-list')

class Kafka_UpdateViewSet(Base_UpdateViewSet):
    model = Kafka
    form_class = forms.KafkaForm
    success_url = reverse_lazy('kafka-list')
    template_name = 'api/kafka_form.html'


class MQ_ViewSet(Base_ListViewSet):
    RocketMQ.objects.all().count()
    model = RocketMQ
    template_name = 'api/mq.html'
    paginate_by = 10

    def get_queryset(self):
        try:
            keyword=self.request.GET['keyword']
        except:
            keyword=''

        if keyword:
            return RocketMQ.objects.select_related().filter(host__name=keyword)
        else:
            return RocketMQ.objects.all()

class MQ_CreateViewSet(Base_CreateViewSet):
    model = RocketMQ
    form_class = forms.MqForm
    template_name = 'api/mq_form.html'
    success_url = reverse_lazy('mq-list')

class MQ_UpdateViewSet(Base_UpdateViewSet):
    model = RocketMQ
    form_class = forms.MqForm
    success_url = reverse_lazy('mq-list')
    template_name = 'api/mq_form.html'



class Item_name_ViewSet(Base_ListViewSet):
    Item_name.objects.all().count()
    model = Item_name
    template_name = 'api/item_name.html'
    paginate_by = 10

    def get_queryset(self):
        query_list=[]
        try:
            keyword=self.request.GET['keyword']
            query_list.append(Q(module__icontains=keyword))
        except:
            pass
        try:
            dev_owner=self.request.GET['dev_owner']
            query_list.append(Q(dev_owner=dev_owner))
        except:
            pass

        if query_list:
            return list(set(Item_name.objects.select_related().filter(reduce(operator.and_, query_list))))
        else:
            return Item_name.objects.all()

class Item_name_CreateViewSet(Base_CreateViewSet):
    model = Item_name
    form_class = forms.Item_nameForm
    template_name = 'api/item_name_form.html'
    success_url = reverse_lazy('item-name-list')

class Item_name_UpdateViewSet(Base_UpdateViewSet):
    model = Item_name
    form_class = forms.Item_nameForm
    success_url = reverse_lazy('item-name-list')
    template_name = 'api/item_name_form.html'

class Item_list_ViewSet(Base_ListViewSet):
    Item_list.objects.all().count()
    model = Item_list
    template_name = 'api/item_list.html'
    paginate_by = 10

    def get_queryset(self):
        try:
            keyword=self.request.GET['keyword']
        except:
            keyword=''
        query_list=[]
        if keyword:
            query_list.append(Q(item__module__icontains=keyword))
        try:
            app=self.request.GET['app']
            query_list.append(Q(app__content=app))
        except:
            pass
        try:
            dev_owner=self.request.GET['dev_owner']
            query_list.append(Q(item__dev_owner__icontains=dev_owner))
        except:
            pass
        if query_list:
            return list(set(Item_list.objects.select_related().filter(reduce(operator.and_, query_list))))
        else:
            return Item_list.objects.select_related().all()

class Item_list_CreateViewSet(Base_CreateViewSet):
    model = Item_list
    form_class = forms.Item_listForm
    template_name = 'api/item_list_form.html'
    success_url = reverse_lazy('item-list-list')



class Ops_act_historyViewSet(Base_ListViewSet):
    Ops_act_history.objects.all().count()
    model = Ops_act_history
    template_name = 'api/operator.html'
    paginate_by = 10


class Ops_act_historyCreateViewSet(Base_CreateViewSet):
    model = Ops_act_history
    form_class = forms.Ops_act_historyForm
    template_name = 'api/operator_form.html'
    success_url = reverse_lazy('ops-act-history')

    def get_form(self, data = None, files = None, **kwargs):
        kwargs['creator'] = self.request.user
        return super(Ops_act_historyCreateViewSet, self).get_form(data, files, **kwargs)


class Ops_plan_historyViewSet(Base_ListViewSet):
    Ops_plan_history.objects.all().count()
    model = Ops_plan_history
    template_name = 'api/ops_plan.html'
    paginate_by = 10

    def get_queryset(self):
        query_list=[]
        try:
            keyword=self.request.GET['keyword']
            query_list.append(Q(title__icontains=keyword))
        except:
            pass

        try:
            status=self.request.GET['status']
            query_list.append(Q(status=status))
        except:
            pass
        if query_list:
            return list(set(Ops_plan_history.objects.filter(reduce(operator.and_, query_list))))
        else:
            return Ops_plan_history.objects.all()



class Ops_plan_history_UpdateViewSet(Base_UpdateViewSet):
    model = Ops_plan_history
    form_class = forms.Ops_plan_historyForm
    success_url = reverse_lazy('ops-plan')
    template_name = 'api/ops_plan_form.html'

class Ops_plan_historyCreateViewSet(Base_CreateViewSet):
    model = Ops_plan_history
    form_class = forms.Ops_plan_historyForm
    template_name = 'api/ops_plan_form.html'
    success_url = reverse_lazy('ops-plan')

    def get_form(self, data = None, files = None, **kwargs):
        kwargs['creator'] = self.request.user
        return super(Ops_plan_historyCreateViewSet, self).get_form(data, files, **kwargs)

class Item_list_UpdateViewSet(Base_UpdateViewSet):
    model = Item_list
    form_class = forms.Item_listForm
    success_url = reverse_lazy('item-list-list')
    template_name = 'api/item_list_form.html'


class Item_check_ViewSet(Base_ListViewSet):
    Item_check.objects.all().count()
    model = Item_check
    template_name = 'api/item_check.html'
    paginate_by = 10

    def get_queryset(self):
        try:
            keyword=self.request.GET['keyword']
        except:
            keyword=''

        if keyword:
            return Item_check.objects.select_related().filter(item__content__icontains=keyword)
        else:
            return Item_check.objects.select_related().all()





class Item_check_CreateViewSet(Base_CreateViewSet):
    model = Item_check
    form_class = forms.Item_checkForm
    template_name = 'api/item_check_form.html'
    success_url = reverse_lazy('item-check-list')

class Item_check_UpdateViewSet(Base_UpdateViewSet):
    model = Item_check
    form_class = forms.Item_checkForm
    success_url = reverse_lazy('item-check-list')
    template_name = 'api/item_check_form.html'

class DetailView(TemplateView):
    template_name = u'api/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        pk=kwargs['pk']
        detail=Item_list.objects.select_related().get(id=pk)
        context['pk'] = pk
        context['item'] = detail.item
        context['app'] = detail.app.content
        context['tech'] = detail.tech.content
        context['front_name'] = u'前端'
        context['front_count']=detail.front.all().count()
        context['front']=detail.front.all()
        context['app_name'] = u'应用'
        context['app_count']=detail.app_link.all().count()
        context['app_list']=detail.app_link.all()
        context['mysql_name'] = u'mysql'
        context['mysql_count']=detail.mysql_link.all().count()
        context['mysql']=detail.mysql_link.all()
        context['codis_name'] = u'codis'
        context['codis_count']=detail.codis_link.all().count()
        context['codis']=detail.codis_link.all()
        context['redis_name'] = u'redis'
        context['redis_count']=detail.redis_link.all().count()
        context['redis']=detail.redis_link.all()
        context['sentinel_name'] = u'sentinel'
        context['sentinel_count']=detail.sentinel.all().count()
        context['sentinel']=detail.sentinel.all()
        context['memcache_name'] = u'memcache'
        context['memcache_count']=detail.memcache.all().count()
        context['memcache']=detail.memcache.all()
        context['es_name'] = u'es'
        context['es_count']=detail.es.all().count()
        context['es']=detail.es.all()
        context['mcq_name'] = u'mcq'
        context['mcq_count']=detail.mcq.all().count()
        context['mcq']=detail.mcq.all()
        context['tfs_name'] = u'tfs'
        context['tfs_count']=detail.tfs.all().count()
        context['tfs']=detail.tfs.all()
        context['zookeeper_name'] = u'zookeeper'
        context['zookeeper_count']=detail.zookeeper.all().count()
        context['zookeeper']=detail.zookeeper.all()
        context['kafka_name'] = u'kafka'
        context['kafka_count']=detail.kafka.all().count()
        context['kafka']=detail.kafka.all()
        context['mq_name'] = u'mq'
        context['mq_count']=detail.mq.all().count()
        context['mq']=detail.mq.all()

        context['remark']=detail.remark
        context['upstream']=detail.upstream
        context['location']=detail.item.location
        context['check_name']=list(set([ x.type.content for x in Item_check.objects.filter(item=detail.item)]))
        context['check_count']=Item_check.objects.filter(item=detail.item).count()
        # context['check_name']=Item_check.objects.filter(item=detail.item).values('type').distinct()
        context['check_list']=Item_check.objects.filter(item=detail.item)
        context['active']=u'item'

        return context


def Item_query(req):
    try:
        name=req.GET['name']
        host=Ipv4Address.objects.get(name=name)
        item_list=[]
        for m in host.front.all():
                front_tmp={}
                front_tmp['item']=m.item
                front_tmp['app']=m.app.content
                front_tmp['name']='front'
                front_tmp['link']=name
                item_list.append(front_tmp)

        for m in host.mysql_link.select_related().all():
            for mysql_n in m.mysql.all():
                mysql_tmp={}
                mysql_tmp['item']=mysql_n.item
                mysql_tmp['app']=mysql_n.app.content
                mysql_tmp['name']='mysql'
                mysql_tmp['link']=m
                item_list.append(mysql_tmp)

        for m in host.app_link.select_related().all():
            for app_n in m.app.all():
                app_tmp={}
                app_tmp['item']=app_n.item
                app_tmp['app']=app_n.app.content
                app_tmp['name']='app'
                app_tmp['link']=m
                item_list.append(app_tmp)

        for m in host.redis_link.select_related().all():
            for redis_n in m.redis.all():
                redis_tmp={}
                redis_tmp['item']=redis_n.item
                redis_tmp['app']=redis_n.app.content
                redis_tmp['name']='redis'
                redis_tmp['link']=m
                item_list.append(redis_tmp)
        for m in host.codis_link.select_related().all():
            for codis_n in m.codis.all():
                codis_tmp={}
                codis_tmp['item']=codis_n.item
                codis_tmp['app']=codis_n.app.content
                codis_tmp['name']='codis'
                codis_tmp['link']=m
                item_list.append(codis_tmp)
        for m in host.sentinel_link.select_related().all():
            for sentinel_n in m.sentinel.all():
                sentinel_tmp={}
                sentinel_tmp['item']=sentinel_n.item
                sentinel_tmp['app']=sentinel_n.app.content
                sentinel_tmp['name']='sentinel'
                sentinel_tmp['link']=m
                item_list.append(sentinel_tmp)
        for m in host.memcache_link.select_related().all():
            for memcache_n in m.memcache.all():
                memcache_tmp={}
                memcache_tmp['item']=memcache_n.item
                memcache_tmp['app']=memcache_n.app.content
                memcache_tmp['name']='memcache'
                memcache_tmp['link']=m
                item_list.append(memcache_tmp)
        for m in host.es_link.select_related().all():
            for es_n in m.es.all():
                es_tmp={}
                es_tmp['item']=es_n.item
                es_tmp['app']=es_n.app.content
                es_tmp['name']='es'
                es_tmp['link']=m
                item_list.append(es_tmp)
        for m in host.mcq_link.select_related().all():
            for mcq_n in m.mcq.all():
                mcq_tmp={}
                mcq_tmp['item']=mcq_n.item
                mcq_tmp['app']=mcq_n.app.content
                mcq_tmp['name']='mcq'
                mcq_tmp['link']=m
                item_list.append(mcq_tmp)
        for m in host.tfs_link.select_related().all():
            for tfs_n in m.tfs.all():
                tfs_tmp={}
                tfs_tmp['item']=tfs_n.item
                tfs_tmp['app']=tfs_n.app.content
                tfs_tmp['name']='tfs'
                tfs_tmp['link']=m
                item_list.append(tfs_tmp)
        for m in host.zoo_link.select_related().all():
            for zoo_n in m.zookeeper.all():
                zoo_tmp={}
                zoo_tmp['item']=zoo_n.item
                zoo_tmp['app']=zoo_n.app.content
                zoo_tmp['name']='zookeeper'
                zoo_tmp['link']=m
                item_list.append(zoo_tmp)
        for m in host.kafka_link.select_related().all():
            for kafka_n in m.kafka.all():
                kafka_tmp={}
                kafka_tmp['item']=kafka_n.item
                kafka_tmp['app']=kafka_n.app.content
                kafka_tmp['name']='kafka'
                kafka_tmp['link']=m
                item_list.append(kafka_tmp)
        for m in host.mq_link.select_related().all():
            for mq_n in m.mq.all():
                mq_tmp={}
                mq_tmp['item']=mq_n.item
                mq_tmp['app']=mq_n.app.content
                mq_tmp['name']='RocketMQ'
                mq_tmp['link']=m
                item_list.append(mq_tmp)

        response = render(req,'api/item_query.html',
                          {
                              "item_list":item_list,
                              "item_count":list(set([x.get('item') for x in item_list])).__len__(),
                              "app_count":list(set([x.get('app') for x in item_list])).__len__(),
                              "name_count":list(set([x.get('name') for x in item_list])).__len__(),
                              "link_count":list(set([x.get('link') for x in item_list])).__len__(),
                              "active":u'api',
                                                  }
                          )
        return response
    except:
        item_list=[]
        response = render(req,'api/item_query.html',{"item_list":item_list,
                                                     "active":u'api',
                                          }
                  )
        return response


class Item_ComponentsView(TemplateView):
    template_name = u'api/components.html'

    def get_context_data(self, **kwargs):
        context = super(Item_ComponentsView, self).get_context_data(**kwargs)
        all_item=Item_list.objects.select_related().all()
        context['mysql'] = [ x for x in all_item if x.mysql_link.all().__len__() != 0]
        context['redis'] = [ x for x in all_item if x.redis_link.all().__len__() != 0]
        context['codis'] = [ x for x in all_item if x.codis_link.all().__len__() != 0]
        context['sentinel'] = [ x for x in all_item if x.sentinel.all().__len__() != 0]
        context['zookeeper'] = [ x for x in all_item if x.zookeeper.all().__len__() != 0]
        context['kafka'] = [ x for x in all_item if x.kafka.all().__len__() != 0]
        context['mq'] = [ x for x in all_item if x.mq.all().__len__() != 0]
        context['memcache'] = [ x for x in all_item if x.memcache.all().__len__() != 0]
        context['es'] = [ x for x in all_item if x.es.all().__len__() != 0]
        context['mcq'] = [ x for x in all_item if x.mcq.all().__len__() != 0]
        context['tfs'] = [ x for x in all_item if x.tfs.all().__len__() != 0]
        context['front'] = [ x for x in all_item if x.front.all().__len__() != 0]
        context['active'] = u'item'
        return context

class Item_deploy_detailView(TemplateView):
    template_name = u'api/deploy_detail.html'

    def get_context_data(self, **kwargs):
        context = super(Item_deploy_detailView, self).get_context_data(**kwargs)
        all_item=Item_list.objects.select_related().all()
        site_all=list(set([x.app for x in all_item]))
        mysql_all_list=[x.mysql_link.all() for x in all_item]
        all_host=[]
        mysql_all=[]
        ### get mysql
        for mysql_p in mysql_all_list:
            for mysql_p_n in mysql_p:
                mysql_all.append(mysql_p_n)

        for mysql_host in mysql_all:
            all_host.append(mysql_host.host.name)
            for mysql_slave in mysql_host.slaveof.all():
                all_host.append(mysql_slave.name)

        ### get front
        front_all_list=[x.front.all() for x in all_item]
        front_all=[]
        for front_p in front_all_list:
            for front_p_n in front_p:
                front_all.append(front_p_n)

        for front_host in front_all:
            all_host.append(front_host.name)


        ## get app link
        app_all_list=[x.app_link.all() for x in all_item]
        app_all=[]
        for app_p in app_all_list:
            for app_p_n in app_p:
                app_all.append(app_p_n.host.name)

        for app_host in app_all:
            all_host.append(app_host)


        ### get redis
        redis_all_list=[x.redis_link.all() for x in all_item]
        redis_all=[]
        for redis_p in redis_all_list:
            for redis_p_n in redis_p:
                redis_all.append(redis_p_n)

        for redis_host in redis_all:
            all_host.append(redis_host.host.name)
            for redis_slave in redis_host.slaveof.all():
                all_host.append(redis_slave.name)



        ### get sentinel
        sentinel_all_list=[x.sentinel.all() for x in all_item]
        sentinel_all=[]
        for sentinel_p in sentinel_all_list:
            for sentinel_p_n in sentinel_p:
                sentinel_all.append(sentinel_p_n)

        for sentinel_host in sentinel_all:
            all_host.append(sentinel_host.host.name)
            for sentinel_slave in sentinel_host.slaveof.all():
                all_host.append(sentinel_slave.name)

        ### get codis
        codis_all_list=[x.codis_link.all() for x in all_item]
        codis_all=[]
        for codis_p in codis_all_list:
            for codis_p_n in codis_p:
                codis_all.append(codis_p_n)

        for codis_host in codis_all:
            all_host.append(codis_host.host.name)
            for codis_slave in codis_host.slaveof.all():
                all_host.append(codis_slave.name)



        ### get mc
        mc_all_list=[x.memcache.all() for x in all_item]
        mc_all=[]
        for mc_p in mc_all_list:
            for mc_p_n in mc_p:
                mc_all.append(mc_p_n)

        for mc_host in mc_all:
            all_host.append(mc_host.host.name)


        # mc_all_list=[x.memcache.all() for x in all_item]
        # mc_all=[]
        # for mc_p in mc_all_list:
        #     for mc_p_n in mc_p:
        #         mc_all.append(mc_p_n)


        ### get es

        es_all_list=[x.es.all() for x in all_item]
        es_all=[]
        for es_p in es_all_list:
            for es_p_n in es_p:
                es_all.append(es_p_n)

        for es_host in es_all:
            all_host.append(es_host.host.name)

        ## get mcq
        mcq_all_list=[x.mcq.all() for x in all_item]
        mcq_all=[]
        for mcq_p in mcq_all_list:
            for mcq_p_n in mcq_p:
                mcq_all.append(mcq_p_n)

        for mcq_host in mcq_all:
            all_host.append(mcq_host.host.name)

        ## get tfs
        tfs_all_list=[x.tfs.all() for x in all_item]
        tfs_all=[]
        for tfs_p in tfs_all_list:
            for tfs_p_n in tfs_p:
                tfs_all.append(tfs_p_n)

        for tfs_host in tfs_all:
            all_host.append(tfs_host.host.name)

        ### get zookeeper

        zoo_all_list=[x.zookeeper.all() for x in all_item]
        zoo_all=[]
        for zoo_p in zoo_all_list:
            for zoo_p_n in zoo_p:
                zoo_all.append(zoo_p_n)

        for zoo_host in zoo_all:
            all_host.append(zoo_host.host.name)


        ### get kafka
        kafka_all_list=[x.kafka.all() for x in all_item]
        kafka_all=[]
        for kafka_p in kafka_all_list:
            for kafka_p_n in kafka_p:
                kafka_all.append(kafka_p_n)


        for kafka_host in kafka_all:
            all_host.append(kafka_host.host.name)
        ### get mq
        mq_all_list=[x.mq.all() for x in all_item]
        mq_all=[]
        for mq_p in mq_all_list:
            for mq_p_n in mq_p:
                mq_all.append(mq_p_n)

        for mq_host in mq_all:
            all_host.append(mq_host.host.name)

        all_redis_cache=[]
        all_redis_cache.extend(redis_all)
        all_redis_cache.extend(sentinel_all)
        all_redis_cache.extend(codis_all)
        all_redis_cache.extend(mc_all)
        context['site_count'] = site_all.__len__()
        context['site_list'] = site_all
        context['mysql_count'] = list(set(mysql_all)).__len__()
        context['mysql_list'] = list(set(mysql_all))
        context['front_count'] = list(set(front_all)).__len__()
        context['front_list'] = list(set(front_all))
        context['app_count'] = list(set(app_all)).__len__()
        context['app_list'] = list(set(app_all))
        context['redis_cache_count'] = list(set(all_redis_cache)).__len__()
        context['redis_cache_list'] = list(set(all_redis_cache))
        context['all_host_len']=list(set(all_host)).__len__()
        context['all_host']=list(set(all_host))
        context['active']=u'item'
        return context
class Machine_detailView(TemplateView):
    template_name = u'api/machine-detail.html'

    def get_context_data(self, **kwargs):
        context = super(Machine_detailView, self).get_context_data(**kwargs)
        try:
            name=self.request.GET['name']
            host=Ipv4Address.objects.get(name=name)
        except:
            host=''
        if host:
            machine=Machine.objects.get(console_ip=host)
            context['ipv4'] = machine.ipv4.all()
            context['cpu'] = machine.cpu
            context['memory'] = machine.memory
            context['kernel'] = machine.kernel
            context['cpu_number'] = machine.cpu_number
            context['vcpu_number'] = machine.vcpu_number
            context['cpu_core'] = machine.cpu_core
            context['hostname'] = machine.hostname
            context['disk'] = machine.disk
            context['swap'] = machine.swap
            context['product'] = machine.product
            context['selinux'] = machine.selinux
            context['distribution'] = machine.distribution
            context['distribution_version'] = machine.distribution_version
            context['manufacturer'] = machine.manufacturer
            context['serial'] = machine.serial
            context['status'] = machine.status
            context['idc'] = machine.idc
            context['company'] = machine.company
            context['console_ip'] = machine.console_ip.name
            context['active']=u'api'
            context['existed'] = True
            return context
        else:
            context['existed'] = False
            return context

class Fun_queryView(TemplateView):
    template_name = u'api/fun_query.html'

    def get_context_data(self, **kwargs):
        context = super(Fun_queryView, self).get_context_data(**kwargs)
        try:
            name=self.request.GET['name']
            host=Ipv4Address.objects.get(name=name)
        except:
            host=''
        if host:
            # context['nginx'] = host.nginx_link.select_related().all()
            item_list=[]
            context['mysql'] = host.mysql_link.select_related().all()
            context['app'] = host.app_link.select_related().all()
            context['redis'] = host.redis_link.select_related().all()
            context['codis'] = host.codis_link.select_related().all()
            context['sentinel'] = host.sentinel_link.select_related().all()
            context['memcache'] = host.memcache_link.select_related().all()
            context['es'] = host.es_link.select_related().all()
            context['mcq'] = host.mcq_link.select_related().all()
            context['tfs'] = host.tfs_link.select_related().all()
            context['item_list']=list(set(item_list))
            summary_list=['mysql','app','redis','codis','sentinel','memcache','es','mcq','tfs']
            summary_info=[ "{0}:{1}".format(x,context.get(x).count()) for x in summary_list if context.get(x).count()!=0]
            context['summary']='|'.join(summary_info)
            context['active']=u'api'

            return context
        else:
            return context


class DNS_checkView(TemplateView):
    template_name = u'api/dns_check.html'

    def get_context_data(self, **kwargs):
        context = super(DNS_checkView, self).get_context_data(**kwargs)
        try:
            domain_name=self.request.GET['name'].strip()
            import DNS
            s = DNS.Request(name=domain_name, server='10.99.73.5')
            resolve = s.req().answers
            all_host=[x.get('data') for x in resolve if x.get('typename')=='A']
            logger.debug(resolve)

        except:
            domain_name=None
            all_host=[]
        # context['domain_name'] = domain_name
        # context['dns_report'] = all_host
        # context['machine'] = Machine.objects.filter(Q(ips__name__in=all_host))
        if domain_name:
            context['result'] = [{"domain":domain_name,"data":x,"host":Machine.objects.filter(Q(ips__name=x))} for x in all_host]
        else:
            context['result']=[]
        context['active']=u'check'
        return context


class Docker_list_ViewSet(Base_ListViewSet):
    Docker_list.objects.all().count()
    model = Docker_list
    template_name = 'api/docker.html'
    paginate_by = 10


    def get_queryset(self):
        try:
            keyword=self.request.GET['keyword']
        except:
            keyword=''

        if keyword:
            return Docker_list.objects.select_related().filter(item__content__istartswith=keyword)
        else:
            return Docker_list.objects.select_related().all()

class Docker_list_CreateViewSet(Base_CreateViewSet):
    model = Docker_list
    form_class = forms.Docker_listForm
    template_name = 'api/docker_form.html'
    success_url = reverse_lazy('docker-list')

class Docker_list_UpdateViewSet(Base_UpdateViewSet):
    model = Docker_list
    form_class = forms.Docker_listForm
    success_url = reverse_lazy('docker-list')
    template_name = 'api/docker_form.html'




@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
def Docker_stop_view(req,pk):
    """
    change the exec-content-status include the times,order,host_done,status
    :param req:
    :return:
    """
    queue=Docker_list.objects.get(id=pk).host.name
    try:
        MissionTask().apply_async(args=(pk,'stop'),queue=queue)
        return HttpResponseRedirect('/docker/')
        # return HttpResponseBadRequest('can not add to queue')
    except Exception,e:
        return HttpResponseBadRequest('can not add to queue')


@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
def Docker_start_view(req,pk):
    """
    change the exec-content-status include the times,order,host_done,status
    :param req:
    :return:
    """
    queue=Docker_list.objects.get(id=pk).host.name
    try:
        MissionTask().apply_async(args=(pk,'start'),queue=queue)
        return HttpResponseRedirect('/docker/')
        # return HttpResponseBadRequest('can not add to queue')
    except Exception,e:
        return HttpResponseBadRequest('can not add to queue')

@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
def Docker_create_view(req,pk):
    """
    change the exec-content-status include the times,order,host_done,status
    :param req:
    :return:
    """
    queue=Docker_list.objects.get(id=pk).host.name
    try:
        MissionTask().apply_async(args=(pk,'create'),queue=queue)
        return HttpResponseRedirect('/docker/')
        # return HttpResponseBadRequest('can not add to queue')
    except Exception,e:
        return HttpResponseBadRequest('can not add to queue')

@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
def Docker_rm_view(req,pk):
    """
    change the exec-content-status include the times,order,host_done,status
    :param req:
    :return:
    """
    queue=Docker_list.objects.get(id=pk).host.name
    try:
        MissionTask().apply_async(args=(pk,'rm'),queue=queue)
        return HttpResponseRedirect('/docker/')
        # return HttpResponseBadRequest('can not add to queue')
    except Exception,e:
        return HttpResponseBadRequest('can not add to queue')