# encoding: utf8

from django.conf.urls import patterns, url
from rest_framework import routers
from api import views

# router = routers.DefaultRouter(trailing_slash=False)
router = routers.DefaultRouter()

router.register(r'ipv4address', views.Ipv4Address_ApiViewSet)
router.register(r'ipv4network', views.Ipv4Network_ApiViewSet)
router.register(r'machine_info', views.Machine_ApiViewSet)
router.register(r'site', views.Site_ApiViewSet)
router.register(r'type', views.Type_name_ApiViewSet)
router.register(r'nginx', views.Nginx_ApiViewSet)
router.register(r'mysql', views.Mysql_ApiViewSet)
router.register(r'application', views.Application_ApiViewSet)
router.register(r'codis', views.Codis_ApiViewSet)
router.register(r'redis', views.Redis_ApiViewSet)
router.register(r'sentinel', views.Sentinel_ApiViewSet)
router.register(r'memcached', views.Memcached_ApiViewSet)
router.register(r'es', views.Es_ApiViewSet)
router.register(r'mcq', views.Mcq_ApiViewSet)
router.register(r'tfs', views.Tfs_ApiViewSet)
router.register(r'item_name', views.Item_name_ApiViewSet)
router.register(r'item_list', views.Item_list_ApiViewSet)

urlpatterns = router.urls