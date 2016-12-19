# #coding=utf8
from django_select2.forms import (
    HeavySelect2MultipleWidget, HeavySelect2Widget, ModelSelect2MultipleWidget,
    ModelSelect2TagWidget, ModelSelect2Widget, Select2MultipleWidget,
    Select2Widget
)

class BaseSearchFieldMixin(object):
    pass

class BaseModelSelect2MultipleWidget(BaseSearchFieldMixin, ModelSelect2MultipleWidget):
    pass

class BaseModelSelect2Widget(BaseSearchFieldMixin, ModelSelect2Widget):
    pass

class IpsModelSelect2MultipleWidget(BaseModelSelect2MultipleWidget):
    search_fields = [
        'name__istartswith',
        'pk__startswith',
    ]

class App_namesModelSelect2MultipleWidget(BaseModelSelect2MultipleWidget):
    search_fields = [
        'content__istartswith',
        'pk__startswith',
    ]

class App_linksModelSelect2MultipleWidget(BaseModelSelect2MultipleWidget):
    search_fields = [
        'host__name__istartswith',
        'pk__startswith',
    ]

class Mysql_linksModelSelect2MultipleWidget(BaseModelSelect2MultipleWidget):
    search_fields = [
        'host__name__istartswith',
        'pk__startswith',
    ]

class Redis_linksModelSelect2MultipleWidget(BaseModelSelect2MultipleWidget):
    search_fields = [
        'host__name__istartswith',
        'pk__startswith',
    ]

class Codis_linksModelSelect2MultipleWidget(BaseModelSelect2MultipleWidget):
    search_fields = [
        'host__name__istartswith',
        'pk__startswith',
    ]

class SentinelModelSelect2MultipleWidget(BaseModelSelect2MultipleWidget):
    search_fields = [
        'host__name__istartswith',
        'pk__startswith',
    ]
class MemcacheModelSelect2MultipleWidget(BaseModelSelect2MultipleWidget):
    search_fields = [
        'host__name__istartswith',
        'pk__startswith',
    ]
class EsModelSelect2MultipleWidget(BaseModelSelect2MultipleWidget):
    search_fields = [
        'host__name__istartswith',
        'pk__startswith',
    ]

class McqModelSelect2MultipleWidget(BaseModelSelect2MultipleWidget):
    search_fields = [
        'host__name__istartswith',
        'pk__startswith',
    ]

class ZookeeperModelSelect2MultipleWidget(BaseModelSelect2MultipleWidget):
    search_fields = [
        'host__name__istartswith',
        'pk__startswith',
    ]

class KafkaModelSelect2MultipleWidget(BaseModelSelect2MultipleWidget):
    search_fields = [
        'host__name__istartswith',
        'pk__startswith',
    ]

class MQModelSelect2MultipleWidget(BaseModelSelect2MultipleWidget):
    search_fields = [
        'host__name__istartswith',
        'pk__startswith',
    ]

class TfsModelSelect2MultipleWidget(BaseModelSelect2MultipleWidget):
    search_fields = [
        'host__name__istartswith',
        'pk__startswith',
    ]

class IpModelSelect2Widget(BaseModelSelect2Widget):
    search_fields = [
        'name__istartswith',
        'pk__startswith',
    ]

class Item_nameModelSelect2Widget(BaseModelSelect2Widget):
    search_fields = [
        'module__istartswith',
        'pk__startswith',
    ]

class App_nameModelSelect2Widget(BaseModelSelect2Widget):
    search_fields = [
        'content__istartswith',
        'pk__startswith',
    ]

class Tech_typeModelSelect2Widget(BaseModelSelect2Widget):
    search_fields = [
        'content__istartswith',
        'pk__startswith',
    ]

class TypeModelSelect2Widget(BaseModelSelect2Widget):
    search_fields = [
        'content__istartswith',
        'pk__startswith',
    ]

class Check_TypeModelSelect2Widget(BaseModelSelect2Widget):
    search_fields = [
        'content__istartswith',
        'pk__startswith',
    ]