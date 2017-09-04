from django.conf.urls import include, url
# from django.contrib import admin
from webui import views
from webui.forms import LoginForm
# from info_api.models import List
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    # url(r'^mission/create/$',views.CreateMissionView,name='mission-create'),
    #edit by guziqiang
    url(r'^$',views.index,name='index'),
    ###dc
    url(r'^machine/$',login_required(views.Machine_listViewSet.as_view()),name='machine-list'),
    url(r'^machine/update/(?P<pk>\d+)/$',login_required(views.Machine_updateViewSet.as_view()),name='machine-update'),
    url(r'^machine/create/$',login_required(views.Machine_createViewSet.as_view()),name='machine-create'),

    ##app
    url(r'^site/$',login_required(views.Site_ViewSet.as_view()),name='site-list'),
    url(r'^site/create/$',permission_required('api.add_site')(views.Site_CreateViewSet.as_view()),name='site-create'),
    url(r'^site/update/(?P<pk>\d+)/$',permission_required('api.change_site')(views.Site_UpdateViewSet.as_view()),name='site-update'),

    ##nginx
    url(r'^nginx/$',login_required(views.Nginx_ViewSet.as_view()),name='nginx-list'),
    url(r'^nginx/create/$',permission_required('api.add_nginx')(views.Nginx_CreateViewSet.as_view()),name='nginx-create'),
    url(r'^nginx/update/(?P<pk>\d+)/$',permission_required('api.change_nginx')(views.Nginx_UpdateViewSet.as_view()),name='nginx-update'),

    ###tech
    url(r'^tech/$',login_required(views.Tech_ViewSet.as_view()),name='tech-list'),
    url(r'^tech/update/(?P<pk>\d+)/$',login_required(views.Tech_UpdateViewSet.as_view()),name='tech-update'),
    url(r'^tech/create/$',login_required(views.Tech_CreateViewSet.as_view()),name='tech-create'),

    ###mysql-link
    url(r'^mysql/$',login_required(views.Mysql_ViewSet.as_view()),name='mysql-list'),
    url(r'^mysql/update/(?P<pk>\d+)/$',login_required(views.Mysql_UpdateViewSet.as_view()),name='mysql-update'),
    url(r'^mysql/create/$',login_required(views.Mysql_CreateViewSet.as_view()),name='mysql-create'),

    ###mapp-link
    url(r'^application/$',login_required(views.Application_ViewSet.as_view()),name='application-list'),
    url(r'^application/update/(?P<pk>\d+)/$',login_required(views.Application_UpdateViewSet.as_view()),name='application-update'),
    url(r'^application/create/$',login_required(views.Application_CreateViewSet.as_view()),name='application-create'),

    ###codis-link
    url(r'^codis/$',login_required(views.Codis_ViewSet.as_view()),name='codis-list'),
    url(r'^codis/update/(?P<pk>\d+)/$',login_required(views.Codis_UpdateViewSet.as_view()),name='codis-update'),
    url(r'^codis/create/$',login_required(views.Codis_CreateViewSet.as_view()),name='codis-create'),


    ### sentinel
    url(r'^sentinel/$',login_required(views.Sentinel_ViewSet.as_view()),name='sentinel-list'),
    url(r'^sentinel/update/(?P<pk>\d+)/$',login_required(views.Sentinel_UpdateViewSet.as_view()),name='sentinel-update'),
    url(r'^sentinel/create/$',login_required(views.Sentinel_CreateViewSet.as_view()),name='sentinel-create'),

    ### redis
    url(r'^redis/$',login_required(views.Redis_ViewSet.as_view()),name='redis-list'),
    url(r'^redis/update/(?P<pk>\d+)/$',login_required(views.Redis_UpdateViewSet.as_view()),name='redis-update'),
    url(r'^redis/create/$',login_required(views.Redis_CreateViewSet.as_view()),name='redis-create'),

    ### memcache
    url(r'^memcache/$',login_required(views.Memcache_ViewSet.as_view()),name='memcache-list'),
    url(r'^memcache/update/(?P<pk>\d+)/$',login_required(views.Memcache_UpdateViewSet.as_view()),name='memcache-update'),
    url(r'^memcache/create/$',login_required(views.Memcache_CreateViewSet.as_view()),name='memcache-create'),


    ### es
    url(r'^es/$',login_required(views.Es_ViewSet.as_view()),name='es-list'),
    url(r'^es/update/(?P<pk>\d+)/$',login_required(views.Es_UpdateViewSet.as_view()),name='es-update'),
    url(r'^es/create/$',login_required(views.Es_CreateViewSet.as_view()),name='es-create'),


    ### mcq
    url(r'^mcq/$',login_required(views.Mcq_ViewSet.as_view()),name='mcq-list'),
    url(r'^mcq/update/(?P<pk>\d+)/$',login_required(views.Mcq_UpdateViewSet.as_view()),name='mcq-update'),
    url(r'^mcq/create/$',login_required(views.Mcq_CreateViewSet.as_view()),name='mcq-create'),


    ### tfs
    url(r'^tfs/$',login_required(views.Tfs_ViewSet.as_view()),name='tfs-list'),
    url(r'^tfs/update/(?P<pk>\d+)/$',login_required(views.Tfs_UpdateViewSet.as_view()),name='tfs-update'),
    url(r'^tfs/create/$',login_required(views.Tfs_CreateViewSet.as_view()),name='tfs-create'),

    ### zookeeper
    url(r'^zookeeper/$',login_required(views.Zookeeper_ViewSet.as_view()),name='zookeeper-list'),
    url(r'^zookeeper/update/(?P<pk>\d+)/$',login_required(views.Zookeeper_UpdateViewSet.as_view()),name='zookeeper-update'),
    url(r'^zookeeper/create/$',login_required(views.Zookeeper_CreateViewSet.as_view()),name='zookeeper-create'),


    ### kafka
    url(r'^kafka/$',login_required(views.Kafka_ViewSet.as_view()),name='kafka-list'),
    url(r'^kafka/update/(?P<pk>\d+)/$',login_required(views.Kafka_UpdateViewSet.as_view()),name='kafka-update'),
    url(r'^kafka/create/$',login_required(views.Kafka_CreateViewSet.as_view()),name='kafka-create'),

    ### mq
    url(r'^mq/$',login_required(views.MQ_ViewSet.as_view()),name='mq-list'),
    url(r'^mq/update/(?P<pk>\d+)/$',login_required(views.MQ_UpdateViewSet.as_view()),name='mq-update'),
    url(r'^mq/create/$',login_required(views.MQ_CreateViewSet.as_view()),name='mq-create'),


    ### item-name
    url(r'^item-name/$',login_required(views.Item_name_ViewSet.as_view()),name='item-name-list'),
    url(r'^item-name/update/(?P<pk>\d+)/$',login_required(views.Item_name_UpdateViewSet.as_view()),name='item-name-update'),
    url(r'^item-name/create/$',login_required(views.Item_name_CreateViewSet.as_view()),name='item-name-create'),


    ### item-list
    url(r'^item-list/$',login_required(views.Item_list_ViewSet.as_view()),name='item-list-list'),
    url(r'^item-list/update/(?P<pk>\d+)/$',login_required(views.Item_list_UpdateViewSet.as_view()),name='item-list-update'),
    url(r'^item-list/create/$',login_required(views.Item_list_CreateViewSet.as_view()),name='item-list-create'),

    ### item-check
    url(r'^item-check/$',login_required(views.Item_check_ViewSet.as_view()),name='item-check-list'),
    url(r'^item-check/update/(?P<pk>\d+)/$',login_required(views.Item_check_UpdateViewSet.as_view()),name='item-check-update'),
    url(r'^item-check/create/$',login_required(views.Item_check_CreateViewSet.as_view()),name='item-check-create'),

    ### item-check
    url(r'^ops-plan/$',login_required(views.Ops_plan_historyViewSet.as_view()),name='ops-plan'),
    url(r'^ops-plan/update/(?P<pk>\d+)/$',login_required(views.Ops_plan_history_UpdateViewSet.as_view()),name='ops-plan-update'),
    url(r'^ops-plan/create/$',login_required(views.Ops_plan_historyCreateViewSet.as_view()),name='ops-plan-create'),


    ### item-check
    url(r'^dns-check/$',login_required(views.DNS_checkView.as_view()),name='dns-check'),


    ### ops-act-history
    url(r'^ops-act-hisotry/$',login_required(views.Ops_act_historyViewSet.as_view()),name='ops-act-history'),
    url(r'^ops-act-history/create/$',login_required(views.Ops_act_historyCreateViewSet.as_view()),name='ops-act-history-create'),


    ### docker
    url(r'^docker/$',login_required(views.Docker_list_ViewSet.as_view()),name='docker-list'),
    url(r'^docker/update/(?P<pk>\d+)/$',login_required(views.Docker_list_UpdateViewSet.as_view()),name='docker-update'),
    url(r'^docker/create/$',login_required(views.Docker_list_CreateViewSet.as_view()),name='docker-create'),
    url(r'^docker/stop/(?P<pk>\d+)/$',login_required(views.Docker_stop_view),name='docker-stop'),
    url(r'^docker/start/(?P<pk>\d+)/$',login_required(views.Docker_stop_view),name='docker-start'),
    url(r'^docker/create/(?P<pk>\d+)/$',login_required(views.Docker_stop_view),name='docker-create'),
    url(r'^docker/remove/(?P<pk>\d+)/$',login_required(views.Docker_stop_view),name='docker-remove'),

    ### item-detail
    url(r'^item/detail/(?P<pk>\d+)/$',login_required(views.DetailView.as_view()),name='item-list-detail'),
    url(r'^item/deploy/detail/$',login_required(views.Item_deploy_detailView.as_view()),name='item-deploy-detail'),
    url(r'^fun_query/$',login_required(views.Fun_queryView.as_view()),name='fun-detail'),
    url(r'^item_fun/$',login_required(views.Item_query),name='item-fun'),
    url(r'^components/$',login_required(views.Item_ComponentsView.as_view()),name='components-query'),
    url(r'^machine-detail/$', login_required(views.Machine_detailView.as_view()), name='machine-detail'),

    ### version post
    url(r'^version/post/$', views.Create_VersionViewAdmin.as_view(), name='version-post'),
    url(r'^version/list/$', views.Get_VersionViewAdmin.as_view(), name='version-list'),

    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'webui/login.html',
            'authentication_form': LoginForm,

        },
        name='login',),
    # Django Select2
    url(r'^select2/', include('django_select2.urls')),

    url(r'^logout/$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),
]
