# encoding: utf8

from django.conf.urls import patterns, url
from rest_framework import routers
import views

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'ipv4address', views.Ipv4AddressViewSet)
router.register(r'ipv4network', views.Ipv4NetworkViewSet)
router.register(r'machine', views.MachineViewSet)
router.register(r'site', views.SiteViewSet)
router.register(r'type', views.Type_nameViewSet)
router.register(r'nginx', views.NginxViewSet)
router.register(r'mysql', views.MysqlViewSet)
router.register(r'application', views.ApplicationViewSet)
router.register(r'codis', views.CodisViewSet)
router.register(r'sentinel', views.SentinelViewSet)
router.register(r'memcached', views.MemcachedViewSet)
router.register(r'es', views.EsViewSet)
router.register(r'mcq', views.McqViewSet)
router.register(r'tfs', views.TfsViewSet)
router.register(r'item_name', views.Item_nameViewSet)
router.register(r'item_list', views.Item_listViewSet)

urlpatterns = router.urls