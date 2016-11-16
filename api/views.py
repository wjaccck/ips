# encoding: utf8

from django.db.models import Count
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import permissions
from .models import *
from .serializers import *
# from rest_framework_filters.backends import DjangoFilterBackend

class MachineViewSet(viewsets.ModelViewSet):
    http_method_names = [ 'get','post','patch']
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    permission_classes = (permissions.DjangoModelPermissions,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, )
    filter_fields = ('name','ips')
    search_fields = ('^name', )

class SiteViewSet(viewsets.ModelViewSet):
    http_method_names = [ 'get','post','patch']
    queryset = Site.objects.all()
    serializer_class = Siteserializers
    permission_classes = (permissions.DjangoModelPermissions,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, )
    filter_fields = ('content',)
    search_fields = ('^content', )

class NginxViewSet(viewsets.ModelViewSet):
    http_method_names = [ 'get','post','patch','delete']
    queryset = Nginx.objects.all()
    serializer_class = Nginxserializers
    permission_classes = (permissions.DjangoModelPermissions,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, )
    filter_fields = ('host','file_name')
    search_fields = ('^file_name', )



class TechViewSet(viewsets.ModelViewSet):
    http_method_names = [ 'get','post','patch']
    queryset = Tech.objects.all()
    serializer_class = Techserializers
    permission_classes = (permissions.DjangoModelPermissions,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, )
    filter_fields = ('content',)
    search_fields = ('^content', )

class MysqlViewSet(viewsets.ModelViewSet):
    http_method_names = [ 'get','post','patch']
    queryset = Mysql.objects.all()
    serializer_class = Mysqlserializers
    permission_classes = (permissions.DjangoModelPermissions,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, )
    filter_fields = ('host',)
    search_fields = ('^host__name', )

class ApplicationViewSet(viewsets.ModelViewSet):
    http_method_names = [ 'get','post','patch']
    queryset = Application.objects.all()
    serializer_class = Applicationserializers
    permission_classes = (permissions.DjangoModelPermissions,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, )
    filter_fields = ('host',)
    search_fields = ('^host__name', )

class CodisViewSet(viewsets.ModelViewSet):
    http_method_names = [ 'get','post','patch']
    queryset = Codis.objects.all()
    serializer_class = Codisserializers
    permission_classes = (permissions.DjangoModelPermissions,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, )
    filter_fields = ('host',)
    search_fields = ('^host__name', )

class SentinelViewSet(viewsets.ModelViewSet):
    http_method_names = [ 'get','post','patch']
    queryset = Sentinel.objects.all()
    serializer_class = Sentinelserializers
    permission_classes = (permissions.DjangoModelPermissions,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, )
    filter_fields = ('host',)
    search_fields = ('^host__name', )

class MemcachedViewSet(viewsets.ModelViewSet):
    http_method_names = [ 'get','post','patch']
    queryset = Memcached.objects.all()
    serializer_class = Memcachedserializers
    permission_classes = (permissions.DjangoModelPermissions,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, )
    filter_fields = ('host',)
    search_fields = ('^host__name', )

class EsViewSet(viewsets.ModelViewSet):
    http_method_names = [ 'get','post','patch']
    queryset = Es.objects.all()
    serializer_class = Esserializers
    permission_classes = (permissions.DjangoModelPermissions,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, )
    filter_fields = ('host',)
    search_fields = ('^host__name', )

class McqViewSet(viewsets.ModelViewSet):
    http_method_names = [ 'get','post','patch']
    queryset = Mcq.objects.all()
    serializer_class = Mcqserializers
    permission_classes = (permissions.DjangoModelPermissions,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, )
    filter_fields = ('host',)
    search_fields = ('^host__name', )

class TfsViewSet(viewsets.ModelViewSet):
    http_method_names = [ 'get','post','patch']
    queryset = Tfs.objects.all()
    serializer_class = Tfsserializers
    permission_classes = (permissions.DjangoModelPermissions,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, )
    filter_fields = ('host',)
    search_fields = ('^host__name', )

class Item_nameViewSet(viewsets.ModelViewSet):
    http_method_names = [ 'get','post','patch']
    queryset = Item_name.objects.all()
    serializer_class = Item_nameserializers
    permission_classes = (permissions.DjangoModelPermissions,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, )
    filter_fields = ('content',)
    search_fields = ('^content', )

class Item_listViewSet(viewsets.ModelViewSet):
    http_method_names = [ 'get','post','patch']
    queryset = Item_list.objects.all()
    serializer_class = Item_listserializers
    permission_classes = (permissions.DjangoModelPermissions,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, )
    filter_fields = ('item',)
    search_fields = ('^item', )




class Type_nameViewSet(viewsets.ModelViewSet):
    http_method_names = [ 'get','post','patch']
    queryset = Type_name.objects.all()
    serializer_class = Type_nameserializers
    permission_classes = (permissions.DjangoModelPermissions,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, )
    filter_fields = ('content',)
    search_fields = ('^content', )






class Ipv4AddressViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset=Ipv4Address.objects.select_related('creator', 'last_modified_by')\
                                .all()
    serializer_class = IPv4AddressSerializer

    # Applies permissions
    permission_classes = (permissions.DjangoModelPermissions,)

    # Applies Filters
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, )
    filter_fields = ('name',)
    search_fields = ('^name', )

    def perform_create(self, serializer):
        serializer.save(
            creator = self.request.user,
            last_modified_by = self.request.user
        )
        return super(Ipv4AddressViewSet, self).perform_create(serializer)


class Ipv4NetworkViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset=Ipv4Network.objects.select_related('creator', 'last_modified_by')\
                                .all()
    serializer_class = IPv4NetworkSerializer

    # Applies permissions
    permission_classes = (permissions.DjangoModelPermissions,)

    # Applies Filters
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, )
    filter_fields = ('name', )
    search_fields = ('^name', )

    def perform_create(self, serializer):
        serializer.save(
            creator = self.request.user,
            last_modified_by = self.request.user
        )
        return super(Ipv4NetworkViewSet, self).perform_create(serializer)