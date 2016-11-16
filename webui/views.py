#coding=utf8
from django.shortcuts import render,redirect
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.decorators import api_view, permission_classes
# from django.views.decorators.csrf import csrf_exempt
# Create your views here.
# from django.http import HttpResponseRedirect
from django.db.models import Q
from api.models import *
from vanilla import ListView, CreateView, UpdateView, DeleteView,FormView
from django.http import HttpResponse,HttpResponseBadRequest,HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
# import json
import forms
from django.views.generic import TemplateView,View
# import datetime
# from core.common import logger
from django.db.models.loading import get_app,get_models,get_model
import operator
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from api.tasks import MissionTask

def index(req):
    if req.user.is_authenticated():
        all_count=Machine.objects.all().count()
        product_list=[ x.get('product') for x in Machine.objects.all().values('product').distinct()]
        product=[{"name":x,"number":Machine.objects.filter(product=x).count()} for x in product_list]
        sys_list=[ x.get('major_release') for x in Machine.objects.all().values('major_release').distinct()]
        sys=[{"name":x,"number":Machine.objects.filter(major_release=x).count()} for x in sys_list]
        response = render(req,'webui/index.html',{"username":req.user.last_name,
                                                  "active":"index",
                                                  "total_list":all_count,
                                                  "product":product,
                                                  "sys":sys
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
        idc=self.kwargs['idc']
        print idc
        query_list=[]
        if idc!='all':
            query_list.append(Q(idc=idc))
        try:
            ip=self.request.GET['ip']
            query_list.append(Q(ips__name__istartswith=ip))
        except:
            pass
        try:
            sys_desc=self.request.GET['sys']
            query_list.append(Q(sys_desc__istartswith=sys_desc))
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

        if keyword:
            return Mysql.objects.select_related().filter(host__name=keyword)
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
    form_class = forms.Application
    template_name = 'api/application_form.html'
    success_url = reverse_lazy('application-list')

class Application_UpdateViewSet(Base_UpdateViewSet):
    model = Application
    form_class = forms.Application
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
            return Codis.objects.select_related().filter(host__name=keyword)
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
            return Sentinel.objects.select_related().filter(host__name=keyword)
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

class Item_name_ViewSet(Base_ListViewSet):
    Item_name.objects.all().count()
    model = Item_name
    template_name = 'api/item_name.html'
    paginate_by = 10

    def get_queryset(self):
        try:
            keyword=self.request.GET['keyword']
        except:
            keyword=''

        if keyword:
            return Item_name.objects.select_related().filter(content__icontains=keyword)
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

        if keyword:
            return Item_list.objects.select_related().filter(item__content__icontains=keyword)
        else:
            return Item_list.objects.select_related().all()

class Item_list_CreateViewSet(Base_CreateViewSet):
    model = Item_list
    form_class = forms.Item_listForm
    template_name = 'api/item_list_form.html'
    success_url = reverse_lazy('item-list-list')

class Item_list_UpdateViewSet(Base_UpdateViewSet):
    model = Item_list
    form_class = forms.Item_listForm
    success_url = reverse_lazy('item-list-list')
    template_name = 'api/item_list_form.html'

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
        context['location']=detail.item.location

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